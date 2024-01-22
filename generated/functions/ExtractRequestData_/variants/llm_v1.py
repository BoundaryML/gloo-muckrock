
# This file is autogenerated by the gloo compiler
# Do not edit this file directly
# (skip unused imports)
# ruff: noqa: F401
# flake8: noqa
# pylint: skip-file
# isort: skip_file
from ....clients import GPT4Client
from ....custom_types import FOIARequestData
from ....custom_types import RecordsStatus
from ....custom_types import RequestStatus
from ....custom_types.stringify import StringifyFOIARequestData
from ....custom_types.stringify import StringifyRecordsStatus
from ....custom_types.stringify import StringifyRequestStatus


import typing
import json
from gloo_py import LLMVariant
from gloo_py.stringify import (
    StringifyBase,
    StringifyError,
    StringifyNone,
    StringifyBool,
    StringifyInt,
    StringifyChar,
    StringifyString,
    StringifyFloat,
    StringifyEnum,
    StringifyUnion,
    StringifyOptional,
    StringifyList,
    StringifyClass,
    FieldDescription,
    EnumFieldDescription,
    StringifyRemappedField,
    StringifyCtx
)

prompt = """\
You are analyzing public records correspondence to figure out what the status of the request for public records is. Your job is to extract the information from the government's response and classify the status of the request.

For the requestStatus field, use the following definitions:
{@RequestStatus.values}

For the recordsStatus field, use the following definitions:
{@RecordsStatus.values}

Agency's response to user:
###
{@input}
###

OUTPUT FORMAT:
{@output.json}

JSON:"""

stringifiers: typing.List[typing.Any] = []
def gen_stringify() -> StringifyBase[FOIARequestData]:
    with StringifyCtx():
        stringify_RecordsStatus = StringifyRecordsStatus(MORE_RECORDS_PENDING= StringifyRemappedField(describe='''The agency has indicated that there are more records to be released soon for this request''',),NO_RECORDS_FOUND= StringifyRemappedField(describe='''The agency has indicated that there are no records found for this request''',),RECORDS_FOUND= StringifyRemappedField(describe='''The agency has indicated that there are records found for this request''',),NOT_APPLICABLE= StringifyRemappedField(describe='''The text does not match any other record status. It may be that the request is still in progress.''',),)
        stringifiers.append(stringify_RecordsStatus)
        stringify_RequestStatus = StringifyRequestStatus(IN_PROGRESS= StringifyRemappedField(describe='''The agency accepted the request and is working on it. Use this status if the agency still has more work to do or has records pending, and the status doesn't fit any other status.''',),FIX_REQUIRED= StringifyRemappedField(describe='''The agency has asked the requestor for clarification, to supply additional information, to narrow down a request, or complete an additional task (not including forwarding the request to another agency or interacting with online portal systems) in order to allow them to continue processing the request''',),PAYMENT_REQUIRED= StringifyRemappedField(describe='''The requestor must pay a fee for the agency to continue processing.''',),REQUEST_REJECTED= StringifyRemappedField(describe='''The request has been denied due to legal exemptions, an issue with the request such as it not being specific enough, the request should be forwarded to another agency, or another reason which causes them not to be able to process it.''',),REQUEST_COMPLETED= StringifyRemappedField(describe='''The agency has completed their processing of the request, and has attached any responsive documents (possibly redacted) found, if there are any. Only use this if there is nothing else left to do for either party.''',),INDETERMINATE= StringifyRemappedField(describe='''Use this status if you cannot determine the correct status from the information provided or if the communication is not related to a public records request.''',),)
        stringifiers.append(stringify_RequestStatus)
        stringify_FOIARequestData = StringifyFOIARequestData(dateEstimate= StringifyRemappedField(describe='''An ISO8601 string of the date by which the agency estimates it will complete processing the request. Use null if not present.''',),price= StringifyRemappedField(describe='''The total balance remaining to pay for this request, as a float. Use null if not present.''',),priceDetails= StringifyRemappedField(describe='''A sentence describing what the price is for (e.g. per page or record delivered, etc). null if not present.''',),)
        stringifiers.append(stringify_FOIARequestData)
        OUTPUT_STRINGIFY = stringify_FOIARequestData
         
        return OUTPUT_STRINGIFY

OUTPUT_STRINGIFY = gen_stringify()



def parser_middleware(raw_llm_output: str) -> str:
    return raw_llm_output

def custom_vars() -> typing.Dict[str, str]:
    return {}


async def parser(raw_llm_output: str) -> FOIARequestData:
    return OUTPUT_STRINGIFY.parse(parser_middleware(raw_llm_output))

async def prompt_vars(arg: str) -> typing.Dict[str, str]:
    vars = {
        'input': str(arg),
        
        'output.json': OUTPUT_STRINGIFY.json,
    }
    vars.update(custom_vars())
    for stringify in stringifiers:
        vars.update(**stringify.vars())
    vars.update(**OUTPUT_STRINGIFY.vars())
    return vars

Variantv1 = LLMVariant[str, FOIARequestData](
    'ExtractRequestData', 'v1', prompt=prompt, client=GPT4Client, parser=parser, prompt_vars=prompt_vars)

async def RunVariant_v1(arg: str) -> FOIARequestData:
    return await Variantv1.run(arg)