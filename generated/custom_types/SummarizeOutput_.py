
# This file is autogenerated by the gloo compiler
# Do not edit this file directly
# (skip unused imports)
# ruff: noqa: F401
# flake8: noqa
# pylint: skip-file
# isort: skip_file


import typing
from pydantic import BaseModel
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

class SummarizeOutput(BaseModel):
    main_summary: str
    attachment_summary: typing.Optional[str]
    important_dates: typing.List[str]
    pending_fees: typing.Optional[str]
    next_steps: typing.Optional[str]
    

class StringifySummarizeOutput(StringifyClass[SummarizeOutput]):
    def __init__(self, **update_kwargs: StringifyRemappedField) -> None:
        values: typing.Dict[str, FieldDescription[typing.Any]] = {"main_summary": FieldDescription(name="main_summary", description=None, type_desc=StringifyString()),"attachment_summary": FieldDescription(name="attachment_summary", description=None, type_desc=StringifyOptional(StringifyString())),"important_dates": FieldDescription(name="important_dates", description=None, type_desc=StringifyList(StringifyString())),"pending_fees": FieldDescription(name="pending_fees", description=None, type_desc=StringifyOptional(StringifyString())),"next_steps": FieldDescription(name="next_steps", description=None, type_desc=StringifyOptional(StringifyString())),}
        super().__init__(model=SummarizeOutput, values=values, updates=update_kwargs)
