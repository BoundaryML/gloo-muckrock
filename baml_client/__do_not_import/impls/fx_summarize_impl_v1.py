# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..clients.client_gpt35client import GPT35Client
from ..functions.fx_summarize import BAMLSummarize
from baml_lib._impl.deserializer import Deserializer


# Impl: v1
# Client: GPT35Client
# An implementation of .


__prompt_template = """\
Extract data from the following TEXT that is a request for public records from a government agency.

EXAMPLE STRUCTURE:
Overall summary of main text: 1-4 sentences.
Overall summary of what the correspondence is about if it exists. Only include details about the public records request. No need to include the actual redacted records.
Important dates: 
Any pending fees: 
Whether this agency can work on this request. If not, why not, and who may be able to work on it instead?
Next step for this request:


Agency's response to the request:
###
{arg}
###

Summary of agency's response:\
"""

__input_replacers = {
    "{arg}"
}


# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[str](str)  # type: ignore






@BAMLSummarize.register_impl("v1")
async def v1(arg: str, /) -> str:
    response = await GPT35Client.run_prompt_template(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
    deserialized = __deserializer.from_string(response.generated)
    return deserialized
