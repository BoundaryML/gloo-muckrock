import typing
from gloo_py import GlooLLMTaskInterface, LLMClient, OpenAILLMClient
from ...types import ClassifyRequestInputModel, ClassifyRequestOutputModel
from ...types import (
    StatusModel,
    StatusModel__Definition,
    RecordsStatusModel__Definition,
)
from ...types import ClassificationModel, ClassificationModel__Definition
from .generated import process_request__Definition, VARS
import asyncio
import json


class process_request(GlooLLMTaskInterface):
    """
    This file is autogenerated by gloo.
    Only modify functions that are prefixed with override_.
    Do not change function signatures for any functions as that may lead to unexpected behavior.
    """

    # The default name is the class name.
    # If you want to change it, uncomment the following function.
    # def override_name(self) -> str:
    #    return "process_request"

    # The default client is OpenAILLMClient, gpt-3.5-turbo (latest model), temperature=0.
    # If you want to change it, uncomment the following function.
    #
    # Alternatively, you can configure a global default client.
    #
    # > from gloo_py import set_default_llm_client, OpenAILLMClient
    # > set_default_llm_client(OpenAILLMClient(model_name="gpt-4", temperature=1))
    #
    def override_llm_client(self) -> LLMClient:
        return OpenAILLMClient(model_name="gpt-4", temperature=0)

    def override_prompt(self) -> str:
        # Prompts are auto dedented and trimmed at the start. The end of the prompt is not trimmed.
        return f"""
        You are analyzing public records correspondence to figure out what the status of the request for public records is. Your job is to extract the information from the government's response and classify the status of the request.
         
        For the "requestStatus.requestStatus" field, use the following definitions:
        {VARS.out_Status.cases}

        For the "recordsStatus" field, use the following definitions:
        "MORE_RECORDS_PENDING": The agency has indicated that there are more records to be released soon for this request.
        "NO_RECORDS_FOUND": The agency has indicated that there are no records found for this request.
        "RECORDS_FOUND": The agency has indicated that there are records found for this request.
        "NOT_APPLICABLE": The text does not match any other recordsStatus. It may be that the request is still in progress.


        Agency's response to user:
        ###
        {VARS.input.request}
        ###

        OUTPUT FORMAT:
        {{
            "trackingNumber": string or empty string,
            "dateEstimate": string, as ISO 8601 or empty string,
            "price": int, use -1 if not present,
            "requestStatus": {{
                "reasoning": Show your critical thinking of what things can help you determine the requestStatus.
                "requestStatus": the public records request's status, as described earlier."
            }},
            recordsStatus: The recordsStatus, as described earlier.
        }}

        JSON:
        """

    # Prompt paramters are variables that you can refer to in your prompt using
    # {{var_name}}. These are static, and are not passed in at runtime. variables
    # allow you to segment your prompt into pieces, and query these individual pieces
    # separately in the analytics dashboard.
    #
    # def override_static_vars(self) -> typing.Dict[str, str]:
    #    return {
    #        # Custom fields that can be tracked to easily compare their impact.
    #        "var_name": "some_value"
    #    }

    # If you wish to format the input in your own manner you can do so here.
    # def override_input_vars(self, input: ClassifyRequestInputModel) -> typing.Dict[str, str]:
    #    return {
    #        # Custom fields that can be tracked to easily compare their impact.
    #        "my_custom_var": input
    #    }

    # This function allows you to describe the output format for your data. You can use
    # this to indicate to the LLM what each field actually means.
    # A definition of each schema field may just be "string[]" or "number" for example, or a more natural language explanation like "the name of the user, as a string".
    # You can refer to any definitions you define here in your prompt by using
    # {VARS.output.trackingNumber.dfn}
    def override_output_definitions(self) -> process_request__Definition:
        return process_request__Definition(
            **{
                "RecordsStatus": RecordsStatusModel__Definition(
                    alias="Status",
                    definition="string",
                    case_name_formatter=lambda name: name,
                    case_formatter=lambda name, desc: f"{name}: {desc}",
                    cases={
                        "MORE_RECORDS_PENDING": {
                            "alias": "MORE_RECORDS_PENDING",
                            "definition": "The agency has indicated that there are more records to be released soon for this request",
                        },
                        "NO_RECORDS_FOUND": {
                            "alias": "NO_RECORDS_FOUND",
                            "definition": "The agency has indicated that there are no records found for this request",
                        },
                        "RECORDS_FOUND": {
                            "alias": "RECORDS_FOUND",
                            "definition": "The agency has indicated that there are records found for this request",
                        },
                        "NOT_APPLICABLE": {
                            "alias": "NOT_APPLICABLE",
                            "definition": "The text does not match any other recordsStatus. It may be that the request is still in progress.",
                        },
                    },
                ),
                "Status": StatusModel__Definition(
                    alias="Status",
                    definition="string",
                    case_name_formatter=lambda name: name,
                    case_formatter=lambda name, desc: f"{name}: {desc}",
                    cases={
                        "REQUEST_REJECTED": {
                            "alias": "REQUEST_REJECTED",
                            "definition": "The request has been denied or needs to be re-routed elsewhere, and no search was done.",
                        },
                        "IN_PROGRESS": {
                            "alias": "IN_PROGRESS",
                            "definition": "The agency accepted the request and is now working on it.",
                        },
                        "FIX_REQUIRED": {
                            "alias": "FIX_REQUIRED",
                            "definition": "The agency has asked the requestor for clarification, to supply additional information, to narrow down a request, or complete an additional task in order to allow them to continue processing the request",
                        },
                        "PAYMENT_REQUIRED": {
                            "alias": "PAYMENT_REQUIRED",
                            "definition": "The requestor must pay a fee for the agency to continue processing.",
                        },
                        "REQUEST_COMPLETED": {
                            "alias": "REQUEST_COMPLETED",
                            "definition": "The text indicates that a response to the public record request is now attached or completed and some records were found (even if they are redacted). If there is nothing else for the agency or the user to do, then this is the correct status.",
                        },
                        "PENDING_MORE_DOCS": {
                            "alias": "PENDING_MORE_DOCS",
                            "definition": "Only choose this if the agency has explicitly stated that they will be releasing more documents in the future.",
                        },
                        "INDETERMINATE": {
                            "alias": "INDETERMINATE",
                            "definition": "Use this status if you cannot determine the correct status from the information provided.",
                        },
                    },
                ),
                "Classification": {
                    # "clues": {
                    #     "alias": "clues",
                    #     "definition": "a couple of sentences from the text that tell us about the status of this request",
                    # },
                    "reasoning": {
                        "alias": "reasoning",
                        "definition": "A sentence describing what status the request may be in and why",
                    },
                    "requestStatus": {
                        "alias": "status",
                        "definition": "string, the best matching public-records request status using the REASONING, and INPUT",
                    },
                },
                "ClassifyRequestOutput": {
                    "trackingNumber ": {
                        "alias": "trackingNumber",
                        "definition": "string",
                    },
                    "dateEstimate": {
                        "alias": "dateEstimate",
                        "definition": "string",
                    },
                    "price": {
                        "alias": "price",
                        "definition": "int",
                    },
                    "classification": {
                        "alias": "classification",
                        "definition": "string",
                    },
                    "reasoning": {
                        "alias": "reasoning",
                        "definition": "string",
                    },
                },
            }
        )

    # By default we assume the model outputs json and we parse it using the pydantic model.
    # GlooLLMTaskInterface.parse_raw converts aliases to their field names.
    # Highly recommend calling super().parse() if you override this function.
    def override_parser(
        self, model: typing.Type[ClassifyRequestOutputModel], raw_llm_response: str
    ) -> ClassifyRequestOutputModel:
        return ClassifyRequestOutputModel.parse_obj(json.loads(raw_llm_response))


# You can add additional parameters to task.run.
# See docs for what paramters work: DOCS_LINK
async def run_process_request_v1_async(
    _in: ClassifyRequestInputModel, **kwargs
) -> ClassifyRequestOutputModel:
    task = process_request()
    return await task.run(_in, output_model=ClassifyRequestOutputModel, **kwargs)


def run_process_request_v1_sync(
    _in: ClassifyRequestInputModel, **kwargs
) -> ClassifyRequestOutputModel:
    return asyncio.run(run_process_request_v1_async(_in, **kwargs))


# Only the run_v1 function is directed exported.
__all__ = [
    "run_process_request_v1_async",
    "run_process_request_v1_sync",
    "ClassifyRequestInputModel",
    "ClassifyRequestOutputModel",
]
