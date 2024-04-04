# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ...enums.enm_recordsstatus import RecordsStatus
from ...enums.enm_requeststatus import RequestStatus
from baml_lib._impl.deserializer import register_deserializer
from pydantic import BaseModel
from typing import Optional


@register_deserializer({  })
class PartialFOIARequestData(BaseModel):
    trackingNumber: Optional[str] = None
    dateEstimate: Optional[str] = None
    price: Optional[float] = None
    priceDetails: Optional[str] = None
    reasoning: Optional[str] = None
    requestStatus: Optional[RequestStatus] = None
    recordsStatus: Optional[RecordsStatus] = None
