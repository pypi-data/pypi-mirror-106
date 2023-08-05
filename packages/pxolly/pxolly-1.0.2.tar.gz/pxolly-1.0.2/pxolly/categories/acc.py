from typing import Optional, Union

from attrdict import AttrDict

from pxolly.categories.base import BaseCategory

from ..models import AccGetInfo

GET_INFO_MODEL = Union[dict, AttrDict, AccGetInfo]


class AccAPICategory(BaseCategory):

    def get_info(self, access_token: Optional[str] = None, is_raw: bool = False) -> GET_INFO_MODEL:
        return self._api.make_request("acc.getInfo", self.get_params(locals()), dataclass=AccGetInfo)

    async def get_info_async(self, access_token: Optional[str] = None, is_raw: bool = False) -> GET_INFO_MODEL:
        return await self._api.make_request_async("acc.getInfo", self.get_params(locals()), dataclass=AccGetInfo)
