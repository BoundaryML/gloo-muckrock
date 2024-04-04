# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_foiarequestdata import FOIARequestData
from ..types.enums.enm_recordsstatus import RecordsStatus
from ..types.enums.enm_requeststatus import RequestStatus
from ..types.partial.classes.cls_foiarequestdata import PartialFOIARequestData
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IExtractRequestDataOutput = FOIARequestData

@runtime_checkable
class IExtractRequestData(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        FOIARequestData
    """

    async def __call__(self, arg: str, /) -> FOIARequestData:
        ...

   

@runtime_checkable
class IExtractRequestDataStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[FOIARequestData, PartialFOIARequestData]
    """

    def __call__(self, arg: str, /) -> AsyncStream[FOIARequestData, PartialFOIARequestData]:
        ...
class BAMLExtractRequestDataImpl:
    async def run(self, arg: str, /) -> FOIARequestData:
        ...
    
    def stream(self, arg: str, /) -> AsyncStream[FOIARequestData, PartialFOIARequestData]:
        ...

class IBAMLExtractRequestData:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IExtractRequestData, IExtractRequestDataStream], None]:
        ...

    async def __call__(self, arg: str, /) -> FOIARequestData:
        ...

    def stream(self, arg: str, /) -> AsyncStream[FOIARequestData, PartialFOIARequestData]:
        ...

    def get_impl(self, name: ImplName) -> BAMLExtractRequestDataImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the ExtractRequestDataInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.ExtractRequestData.mock() as mocked:
                    mocked.return_value = ...
                    result = await ExtractRequestDataImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractRequestDataInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.ExtractRequestData.test
            async def test_logic(ExtractRequestDataImpl: IExtractRequestData) -> None:
                result = await ExtractRequestDataImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractRequestDataInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.ExtractRequestData.test(exclude_impl=["implname"])
            async def test_logic(ExtractRequestDataImpl: IExtractRequestData) -> None:
                result = await ExtractRequestDataImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.ExtractRequestData.test(stream=True)
            async def test_logic(ExtractRequestDataImpl: IExtractRequestDataStream) -> None:
                async for result in ExtractRequestDataImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractRequestDataInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.ExtractRequestData.test
        class TestClass:
            def test_a(self, ExtractRequestDataImpl: IExtractRequestData) -> None:
                ...
            def test_b(self, ExtractRequestDataImpl: IExtractRequestData) -> None:
                ...
        ```
        """
        ...

BAMLExtractRequestData: IBAMLExtractRequestData
