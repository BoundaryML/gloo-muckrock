
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
        stringify_RecordsStatus = StringifyRecordsStatus(MORE_RECORDS_PENDING= StringifyRemappedField(describe='''The agency has indicated that there are more records to be released soon for this reques''',),NO_RECORDS_FOUND= StringifyRemappedField(describe='''The agency has indicated that there are no records found for this request''',),RECORDS_FOUND= StringifyRemappedField(describe='''The agency has indicated that there are records found for this request''',),NOT_APPLICABLE= StringifyRemappedField(describe='''The text does not match any other record status. It may be that the request is still in progress.''',),)
        stringifiers.append(stringify_RecordsStatus)
        stringify_RequestStatus = StringifyRequestStatus(IN_PROGRESS= StringifyRemappedField(describe='''The agency accepted the request and is now working on it.''',),FIX_REQUIRED= StringifyRemappedField(describe='''The agency has asked the requestor for clarification, to supply additional information, to narrow down a request, or complete an additional task in order to allow them to continue processing the request''',),PAYMENT_REQUIRED= StringifyRemappedField(describe='''The requestor must pay a fee for the agency to continue processing.''',),REQUEST_REJECTED= StringifyRemappedField(describe='''The request has been denied or needs to be re-routed elsewhere, and no search for records was done.''',),REQUEST_COMPLETED= StringifyRemappedField(describe='''The text indicates that a response to the public record request is now attached or completed and some records were found (even if they are redacted). If there is nothing else for the agency or the user to do, then this is the correct status''',),PENDING_MORE_DOCS= StringifyRemappedField(describe='''The agency has indicated that there are more records to be released soon for this request.''',),INDETERMINATE= StringifyRemappedField(describe='''Use this status if you cannot determine the correct status from the information provided.''',),)
        stringifiers.append(stringify_RequestStatus)
        stringify_FOIARequestData = StringifyFOIARequestData()
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
