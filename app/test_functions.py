from baml_client.baml_types import (
    FOIARequestData,
    RecordsStatus,
    RequestStatus,
)
from typing import NamedTuple, Optional, Tuple, List
import pytest

from baml_client.testing import baml_test
from . import process_request
import json
from pydantic import BaseModel


class FoiaTestCasePayload(BaseModel):
    name: str
    tid: int
    cid: int
    username: str
    communication: Optional[str]
    file_text: Optional[str]
    status: Optional[str]
    tracking_number: Optional[str]
    date_estimate: Optional[str]
    price: Optional[float]


async def base_test(test_case: FoiaTestCasePayload):
    extracted_data, status = await process_request(
        test_case.communication or "", test_case.file_text or ""
    )
    assert status == test_case.status
    if test_case.price:
        assert extracted_data.price == test_case.price


def load_tests(file):
    with open(file, "r") as f:
        return [FoiaTestCasePayload(**case) for case in json.load(f)]


class TestStatusDone:
    @baml_test
    @pytest.mark.parametrize(
        "test_case", load_tests("tests/test_status_done.json"), ids=lambda x: x.name
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusFix:
    @baml_test
    @pytest.mark.parametrize(
        "test_case", load_tests("tests/test_status_fix.json"), ids=lambda x: x.name
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusIndeterminate:
    @baml_test
    @pytest.mark.parametrize(
        "test_case",
        load_tests("tests/test_status_indeterminate.json"),
        ids=lambda x: x.name,
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusNoDocs:
    @baml_test
    @pytest.mark.parametrize(
        "test_case", load_tests("tests/test_status_no_docs.json"), ids=lambda x: x.name
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusOther:
    @baml_test
    @pytest.mark.parametrize(
        "test_case", load_tests("tests/test_status_other.json"), ids=lambda x: x.name
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusPartial:
    @baml_test
    @pytest.mark.parametrize(
        "test_case", load_tests("tests/test_status_partial.json"), ids=lambda x: x.name
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusPayment:
    @baml_test
    @pytest.mark.parametrize(
        "test_case", load_tests("tests/test_status_payment.json"), ids=lambda x: x.name
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusProcessed:
    @baml_test
    @pytest.mark.parametrize(
        "test_case",
        load_tests("tests/test_status_processed.json"),
        ids=lambda x: x.name,
    )
    async def test_case(self, test_case):
        await base_test(test_case)


class TestStatusRejected:
    @baml_test
    @pytest.mark.parametrize(
        "test_case", load_tests("tests/test_status_rejected.json"), ids=lambda x: x.name
    )
    async def test_case(self, test_case):
        await base_test(test_case)

    # TODO: estimated dates


class TestEstimatedDates:
    @baml_test
    @pytest.mark.parametrize(
        "test_case",
        load_tests("tests/test_date_estimates.json"),
        ids=lambda x: x.name,
    )
    async def test_case(self, test_case):
        extracted_data, status = await process_request(
            test_case.communication or "", test_case.file_text or ""
        )
        if test_case.price:
            assert extracted_data.price == test_case.price

        if test_case.tracking_number:
            assert extracted_data.trackingNumber == test_case.tracking_number

        if test_case.date_estimate:
            assert extracted_data.dateEstimate == test_case.date_estimate
        