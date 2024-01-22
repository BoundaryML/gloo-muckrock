
# This file is autogenerated by the gloo compiler
# Do not edit this file directly
# (skip unused imports)
# ruff: noqa: F401
# flake8: noqa
# pylint: skip-file
# isort: skip_file
from .RecordsStatus_ import RecordsStatus
from .RecordsStatus_ import StringifyRecordsStatus
from .RequestStatus_ import RequestStatus
from .RequestStatus_ import StringifyRequestStatus


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

class FOIARequestData(BaseModel):
    trackingNumber: typing.Optional[str]
    dateEstimate: typing.Optional[str]
    price: typing.Optional[float]
    priceDetails: typing.Optional[str]
    reasoning: str
    requestStatus: RequestStatus
    recordsStatus: RecordsStatus
    

class StringifyFOIARequestData(StringifyClass[FOIARequestData]):
    def __init__(self, **update_kwargs: StringifyRemappedField) -> None:
        values: typing.Dict[str, FieldDescription[typing.Any]] = {"trackingNumber": FieldDescription(name="trackingNumber", description=None, type_desc=StringifyOptional(StringifyString())),"dateEstimate": FieldDescription(name="dateEstimate", description=None, type_desc=StringifyOptional(StringifyString())),"price": FieldDescription(name="price", description=None, type_desc=StringifyOptional(StringifyFloat())),"priceDetails": FieldDescription(name="priceDetails", description=None, type_desc=StringifyOptional(StringifyString())),"reasoning": FieldDescription(name="reasoning", description=None, type_desc=StringifyString()),"requestStatus": FieldDescription(name="requestStatus", description=None, type_desc=StringifyRequestStatus()),"recordsStatus": FieldDescription(name="recordsStatus", description=None, type_desc=StringifyRecordsStatus()),}
        super().__init__(model=FOIARequestData, values=values, updates=update_kwargs)