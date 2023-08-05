from abc import ABC
from typing import Optional

from pxolly.abc import APICategoriesABC

from .acc import AccAPICategory


class APICategories(APICategoriesABC, ABC):

    @property
    def acc(self):
        return AccAPICategory(self.api_instance)

    def execute(
            self,
            code: str,
            access_token: Optional[str] = None,
            is_raw: bool = True,
            dataclass=dict
    ):
        return self.api_instance.make_request(
            'execute',
            {"code": code, "access_token": access_token, "is_raw": is_raw},
            dataclass=dataclass
        )

    async def execute_async(
            self,
            code: str,
            access_token: Optional[str] = None,
            is_raw: bool = True,
            dataclass=dict
    ):
        return await self.api_instance.make_request_async(
            'execute',
            {"code": code, "access_token": access_token, "is_raw": is_raw},
            dataclass=dataclass
        )
