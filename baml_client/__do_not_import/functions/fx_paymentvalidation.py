# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_paymentvalidationdata import PaymentValidationData
from ..types.partial.classes.cls_paymentvalidationdata import PartialPaymentValidationData
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IPaymentValidationOutput = PaymentValidationData

@runtime_checkable
class IPaymentValidation(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        PaymentValidationData
    """

    async def __call__(self, arg: str, /) -> PaymentValidationData:
        ...

   

@runtime_checkable
class IPaymentValidationStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[PaymentValidationData, PartialPaymentValidationData]
    """

    def __call__(self, arg: str, /) -> AsyncStream[PaymentValidationData, PartialPaymentValidationData]:
        ...
class IBAMLPaymentValidation(BaseBAMLFunction[PaymentValidationData, PartialPaymentValidationData]):
    def __init__(self) -> None:
        super().__init__(
            "PaymentValidation",
            IPaymentValidation,
            ["v1"],
        )

    async def __call__(self, *args, **kwargs) -> PaymentValidationData:
        return await self.get_impl("v1").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[PaymentValidationData, PartialPaymentValidationData]:
        res = self.get_impl("v1").stream(*args, **kwargs)
        return res

BAMLPaymentValidation = IBAMLPaymentValidation()

__all__ = [ "BAMLPaymentValidation" ]