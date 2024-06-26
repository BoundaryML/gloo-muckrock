# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..clients.client_gpt4client import GPT4Client
from ..functions.fx_extractrequestdata import BAMLExtractRequestData
from ..types.classes.cls_foiarequestdata import FOIARequestData
from ..types.enums.enm_recordsstatus import RecordsStatus
from ..types.enums.enm_requeststatus import RequestStatus
from ..types.partial.classes.cls_foiarequestdata import PartialFOIARequestData
from baml_core.provider_manager.llm_response import LLMResponse
from baml_core.stream import AsyncStream
from baml_lib._impl.deserializer import Deserializer


import typing
# Impl: v1
# Client: GPT4Client
# An implementation of ExtractRequestData.

__prompt_template = """\
You are analyzing public records correspondence to figure out what the status of the request for public records is. Your job is to extract the information from the government's response and classify the status of the request.

For the requestStatus field, use the following definitions:
RequestStatus
---
IN_PROGRESS: The agency accepted the request and is working on it. Use this status if the agency still has more work to do or has records pending, and the status doesn't fit any other status.
FIX_REQUIRED: The agency has asked the requestor for clarification, to supply additional information, to narrow down a request, or complete an additional task (not including forwarding the request to another agency or interacting with online portal systems) in order to allow them to continue processing the request
PAYMENT_REQUIRED: The requestor must pay a fee for the agency to continue processing.
REQUEST_REJECTED: The request has been denied due to legal exemptions, an issue with the request such as it not being specific enough, the request should be forwarded to another agency, or another reason which causes them not to be able to process it.
REQUEST_COMPLETED: The agency has completed their processing of the request, and has attached any responsive documents (possibly redacted) found, if there are any. Only use this if there is nothing else left to do for either party.
INDETERMINATE: Use this status if you cannot determine the correct status from the information provided or if the communication is not related to a public records request.

For the recordsStatus field, use the following definitions:
RecordsStatus
---
NOT_APPLICABLE: The text does not match any other record status. It may be that the request is still in progress.
RECORDS_FOUND: The agency has indicated that there are records found for this request
NO_RECORDS_FOUND: The agency has indicated that there are no records found for this request
MORE_RECORDS_PENDING: The agency has indicated that there are more records to be released soon for this request

Agency's response to user:
###
{arg}
###

OUTPUT FORMAT:
{
  "trackingNumber": string | null,
  // An ISO8601 string of the date by which the agency estimates it will complete processing the request. Use null if not present.
  "dateEstimate": string | null,
  // The total balance remaining to pay for this request, as a float. Use null if not present.
  "price": float | null,
  // A sentence describing what the price is for (e.g. per page or record delivered, etc). null if not present.
  "priceDetails": string | null,
  "reasoning": string,
  "requestStatus": "RequestStatus as string",
  "recordsStatus": "RecordsStatus as string"
}

JSON:\
"""

__input_replacers = {
    "{arg}"
}


# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[FOIARequestData](FOIARequestData)  # type: ignore

# Add a deserializer that handles stream responses, which are all Partial types
__partial_deserializer = Deserializer[PartialFOIARequestData](PartialFOIARequestData)  # type: ignore







async def v1(arg: str, /) -> FOIARequestData:
    response = await GPT4Client.run_prompt_template(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
    deserialized = __deserializer.from_string(response.generated)
    return deserialized


def v1_stream(arg: str, /) -> AsyncStream[FOIARequestData, PartialFOIARequestData]:
    def run_prompt() -> typing.AsyncIterator[LLMResponse]:
        raw_stream = GPT4Client.run_prompt_template_stream(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
        return raw_stream
    stream = AsyncStream(stream_cb=run_prompt, partial_deserializer=__partial_deserializer, final_deserializer=__deserializer)
    return stream

BAMLExtractRequestData.register_impl("v1")(v1, v1_stream)