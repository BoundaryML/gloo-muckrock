# Standard Library
import json
import logging
import os
from collections import defaultdict
from enum import Enum
from typing import Any, Awaitable, Callable, Dict, List, Tuple

# Third Party
import pandas as pd
import tiktoken
from pydantic import BaseModel

from ..baml_client import baml as b
from ..baml_client.baml_types import FOIARequestData, RecordsStatus, RequestStatus
from ..baml_client.tracing import set_tags, trace


class MRStatus(Enum):
    NO_DOCS = "no_docs"
    PROCESSED = "processed"
    PAYMENT = "payment"
    DONE = "done"
    FIX = "fix"
    ABANDONED = "abandoned"
    APPEALING = "appealing"
    REJECTED = "rejected"
    PARTIAL = "partial"
    INDETERMINATE = "indeterminate"


def map_status_(status: RequestStatus, recordsStatus: RecordsStatus):
    status_mapping = {
        MRStatus.NO_DOCS.value: "",
        MRStatus.PROCESSED.value: "IN_PROGRESS",
        MRStatus.PAYMENT.value: "PAYMENT",
        MRStatus.DONE.value: "DONE",
        MRStatus.FIX.value: "FIX",
        MRStatus.ABANDONED.value: "INDETERMINATE",
        MRStatus.APPEALING.value: "INDETERMINATE",
        MRStatus.REJECTED.value: "REJECTED",
        MRStatus.PARTIAL.value: "PARTIAL",
    }
    return status_mapping.get(status, "INDETERMINATE")


def map_status(data: FOIARequestData) -> MRStatus:
    both = (data.requestStatus, data.recordsStatus)
    req = data.requestStatus

    if both == (RequestStatus.REQUEST_COMPLETED, RecordsStatus.NO_RECORDS_FOUND):
        return MRStatus.NO_DOCS
    elif both == (RequestStatus.REQUEST_COMPLETED, RecordsStatus.RECORDS_FOUND):
        return MRStatus.DONE
    elif both == (RequestStatus.REQUEST_COMPLETED, RecordsStatus.NOT_APPLICABLE):
        return MRStatus.DONE
    elif both == (RequestStatus.IN_PROGRESS, RecordsStatus.MORE_RECORDS_PENDING):
        return MRStatus.PARTIAL
    elif both == (RequestStatus.IN_PROGRESS, RecordsStatus.RECORDS_FOUND):
        return MRStatus.PARTIAL
    elif req == RequestStatus.IN_PROGRESS:
        return MRStatus.PROCESSED
    elif req == RequestStatus.PAYMENT_REQUIRED:
        return MRStatus.PAYMENT
    elif req == RequestStatus.FIX_REQUIRED:
        return MRStatus.FIX
    elif req == RequestStatus.REQUEST_REJECTED:
        return MRStatus.REJECTED
    else:
        return MRStatus.INDETERMINATE


class ExpectedOutput(BaseModel):
    status: RequestStatus
    recordsStatus: RecordsStatus


def expected_gloo_statuses(mrStatus: MRStatus) -> ExpectedOutput:
    status_mapping = {
        MRStatus.NO_DOCS: (
            RequestStatus.REQUEST_COMPLETED,
            RecordsStatus.NO_RECORDS_FOUND,
        ),
        MRStatus.PROCESSED: (
            RequestStatus.IN_PROGRESS,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.PAYMENT: (
            RequestStatus.PAYMENT_REQUIRED,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.DONE: (
            RequestStatus.REQUEST_COMPLETED,
            RecordsStatus.RECORDS_FOUND,
        ),
        MRStatus.FIX: (RequestStatus.FIX_REQUIRED, RecordsStatus.NOT_APPLICABLE),
        MRStatus.ABANDONED: (
            RequestStatus.INDETERMINATE,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.APPEALING: (
            RequestStatus.IN_PROGRESS,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.REJECTED: (
            RequestStatus.REQUEST_REJECTED,
            RecordsStatus.NOT_APPLICABLE,
        ),
        MRStatus.PARTIAL: (
            RequestStatus.IN_PROGRESS,
            RecordsStatus.MORE_RECORDS_PENDING,
        ),
    }
    status, records_status = status_mapping.get(
        mrStatus, (RequestStatus.INDETERMINATE, RecordsStatus.NOT_APPLICABLE)
    )
    return ExpectedOutput(status=status, recordsStatus=records_status)


enc = tiktoken.encoding_for_model("gpt-4")


@trace
async def process_request(
    request_text: str, file_text: str, **tags
) -> (Tuple[FOIARequestData, str]):
    if tags:
        set_tags(**tags)

    if file_text:
        file_text = f"Attached Correspondence:\n{file_text}"
        request_text = f"{request_text}\n{file_text}"

    tokens = enc.encode(request_text)
    ellipsis_tokens = enc.encode("...")
    max_tokens = 2000
    if len(tokens) > max_tokens:
        tokens = tokens[: max_tokens - len(ellipsis_tokens)] + ellipsis_tokens
    request_text = enc.decode(tokens)

    extractedData = await b.ExtractRequestData(
        request_text,
    )
    status = map_status(extractedData)
    set_tags(
        status=status.value,
        has_tracking=str(extractedData.trackingNumber is not None),
        has_date=str(extractedData.dateEstimate is not None),
    )

    return (extractedData, status.value)
