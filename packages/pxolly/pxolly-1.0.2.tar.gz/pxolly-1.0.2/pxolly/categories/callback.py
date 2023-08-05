from typing import Optional, Union

from attrdict import AttrDict

from pxolly.categories.base import BaseCategory

from ..models import CallbackGetSettings

GET_SETTINGS_MODEL = EDIT_SETTINGS_MODEL = Union[dict, AttrDict, CallbackGetSettings]


class CallbackAPICategory(BaseCategory):

    def get_settings(self, access_token: Optional[str] = None, is_raw: bool = False) -> GET_SETTINGS_MODEL:
        return self._api.make_request("callback.getSettings", self.get_params(locals()), dataclass=CallbackGetSettings)

    async def get_settings_async(self, access_token: Optional[str] = None, is_raw: bool = False) -> GET_SETTINGS_MODEL:
        return await self._api.make_request_async(
            "callback.getSettings",
            self.get_params(locals()),
            dataclass=CallbackGetSettings
        )

    def edit_settings(
            self,
            url: str,
            confirmation_code: str,
            secret_key: str,
            access_token: Optional[str] = None,
            is_raw: bool = False
    ) -> EDIT_SETTINGS_MODEL:
        return self._api.make_request("callback.editSettings", self.get_params(locals()), dataclass=CallbackGetSettings)

    async def edit_settings_async(
            self,
            url: str,
            confirmation_code: str,
            secret_key: str,
            access_token: Optional[str] = None,
            is_raw: bool = False
    ) -> EDIT_SETTINGS_MODEL:
        return await self._api.make_request_async(
            "callback.editSettings",
            self.get_params(locals()),
            dataclass=CallbackGetSettings
        )
