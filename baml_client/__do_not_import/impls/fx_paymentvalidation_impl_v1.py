# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..clients.client_gpt4client import GPT4Client
from ..functions.fx_paymentvalidation import BAMLPaymentValidation
from ..types.classes.cls_paymentvalidationdata import PaymentValidationData
from ..types.partial.classes.cls_paymentvalidationdata import PartialPaymentValidationData
from baml_core.provider_manager.llm_response import LLMResponse
from baml_core.stream import AsyncStream
from baml_lib._impl.deserializer import Deserializer


import typing
# Impl: v1
# Client: GPT4Client
# An implementation of PaymentValidation.

__prompt_template = """\
Given this email extract any payment related content

###
{arg}
###

OUTPUT FORMAT:
{
  // The amount of money the agency is requesting, if they have given an amount
  "paymentAmount": float | null,
  // Is the amount of money being requested an estimate?  This is opposed to it being an exact amount.
  "estimate": bool,
  // Is the payment required now, before they will process the request, whether it is an estimate of the final cost or not, or is it just a notice that payment will be required in the future?
  "required": bool,
  // If the payment is required before they will process the request, are they asking for any sort of response before accepting payment, such as how you would like to proceed, confirmation to proceed, if you accept the charges, need to choose between versions of the request, or any other modifications of the request?
  "responseRequired": bool,
  // Is the agency stating they have not yet received payment which was previously asked for.  This should only be true for follow ups to previous requests for payment or invoices, and not for new payment requests.
  "notReceived": bool
}

Before OUTPUT FORMAT, summarize all the payment related content.
Example: 
<summary...>
{
    ...
}\
"""

__input_replacers = {
    "{arg}"
}


# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[PaymentValidationData](PaymentValidationData)  # type: ignore

# Add a deserializer that handles stream responses, which are all Partial types
__partial_deserializer = Deserializer[PartialPaymentValidationData](PartialPaymentValidationData)  # type: ignore







async def v1(arg: str, /) -> PaymentValidationData:
    response = await GPT4Client.run_prompt_template(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
    deserialized = __deserializer.from_string(response.generated)
    return deserialized


def v1_stream(arg: str, /) -> AsyncStream[PaymentValidationData, PartialPaymentValidationData]:
    def run_prompt() -> typing.AsyncIterator[LLMResponse]:
        raw_stream = GPT4Client.run_prompt_template_stream(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
        return raw_stream
    stream = AsyncStream(stream_cb=run_prompt, partial_deserializer=__partial_deserializer, final_deserializer=__deserializer)
    return stream

BAMLPaymentValidation.register_impl("v1")(v1, v1_stream)