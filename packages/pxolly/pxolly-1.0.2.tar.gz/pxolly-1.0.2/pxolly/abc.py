import asyncio
from abc import ABC, abstractmethod
from typing import Dict, Union, Type

from attrdict import AttrDict
from pydantic import BaseModel


class BaseAPICategoriesABC(ABC):
    ...


class APICategoriesABC(ABC):

    @property
    @abstractmethod
    def api_instance(self) -> "PxollyAPIABC":
        ...


class PxollyAPIABC(APICategoriesABC):

    @abstractmethod
    def make_request(
            self,
            method: str,
            data: Dict = None,
            dataclass: Union[Type[dict], Type[AttrDict], Type[BaseModel]] = AttrDict
    ) -> dict:
        ...

    @abstractmethod
    async def make_request_async(
            self,
            method: str,
            data: Dict = None,
            dataclass: Union[Type[dict], Type[AttrDict], Type[BaseModel]] = AttrDict
    ) -> dict:
        ...

    @property
    @abstractmethod
    def loop(self) -> asyncio.AbstractEventLoop:
        ...
