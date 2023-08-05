import asyncio
from typing import Type, TypeVar, Dict, Tuple, Optional, Callable

import aiohttp
import requests
from attrdict import AttrDict
from pydantic import BaseModel, ValidationError

from pxolly import const
from pxolly.abc import PxollyAPIABC
from pxolly.categories import APICategories
from pxolly.exceptions import PxollyAPIException

try:
    from loguru import logger
except ImportError:
    import logging

    logger = logging.getLogger(__name__)

T = TypeVar('T', dict, AttrDict, BaseModel)


class PxollyAPI(PxollyAPIABC, APICategories):
    URL = "https://api.pxolly.ru/method/{method}"
    HEADERS = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    def __init__(
            self,
            token: str = None,
            *,
            loop: asyncio.AbstractEventLoop = None,
            raise_validation_error: bool = False,
            timeout: float = 30,
            data_generator: Callable[["PxollyAPI", Dict], Dict] = lambda api, data: data
    ):
        self._access_token = token
        self._loop = loop
        self.raise_validation_error = raise_validation_error
        self.timeout = timeout
        self._data_generator = data_generator

    def __repr__(self) -> str:
        return (
            f"<PxollyAPI("
            f"raise_validation_error={self.raise_validation_error}, "
            f"timeout={self.timeout}, "
            f"token={'static' if self._access_token else 'dynamic'}"
            f")>"
        )

    @property
    def api_instance(self) -> "PxollyAPI":
        return self

    def make_request(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        request_url, request_data, is_raw = self.get_prepared_data(method, data)
        response = requests.post(request_url, data=request_data, timeout=self.timeout, headers=self.HEADERS)
        response.raise_for_status()
        response_json = response.json()
        return self.validate_response(response_json, dataclass, is_raw)

    async def make_request_async(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        request_url, request_data, is_raw = self.get_prepared_data(method, data)
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
            async with session.post(request_url, data=request_data) as response:
                response.raise_for_status()
                response_json = await response.json()
        return self.validate_response(response_json, dataclass, is_raw)

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        return self._loop

    @loop.setter
    def loop(self, new_loop: asyncio.AbstractEventLoop):
        self._loop = new_loop

    def get_prepared_data(self, method: str, data: Optional[Dict]) -> Tuple[str, Dict, bool]:
        if data is None:
            data = dict()
        data['access_token'] = data.get('access_token', None) or self._access_token
        is_raw = data.pop('is_raw', False)
        data = self._data_generator(self, data)
        url = self.URL.format(method=method)
        logger.debug(f"Data prepared: url is {url}. Data: {self.data_to_print(data)}. Is raw: {is_raw}.")
        return url, data, is_raw

    def validate_response(self, response: Dict, dataclass: Type[T], is_raw: bool = False) -> T:
        logger.debug(f"Response: {response}. Use dataclass {dataclass.__name__}. Raw: {is_raw}")
        if is_raw:
            return response
        if 'error' in response:
            raise PxollyAPIException(**response['error'])
        try:
            data = dataclass(**response['response'])
            logger.debug(f"Response validated with dataclass {dataclass.__name__}")
            return data
        except ValidationError as ex:
            if self.raise_validation_error:
                raise ex
            logger.error(f"ValidationError: Response validated with dataclass AttrDict")
            return AttrDict(response)

    @staticmethod
    def data_to_print(data: Dict) -> Dict:
        new_dict = {}
        for k, v in data.items():
            if k == 'access_token':
                new_dict[k] = v[:4] + '*' * 4 + v[-4:]
            else:
                new_dict[k] = v
        return new_dict

    @property
    def author(self) -> str:
        return const.__author__

    @property
    def version(self) -> str:
        return const.__version__
