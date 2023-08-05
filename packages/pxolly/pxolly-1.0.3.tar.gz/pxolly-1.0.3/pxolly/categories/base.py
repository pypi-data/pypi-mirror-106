from pxolly.abc import BaseAPICategoriesABC, PxollyAPIABC


class BaseCategory(BaseAPICategoriesABC):

    def __init__(self, api: PxollyAPIABC):
        self._api = api

    @staticmethod
    def get_params(local_params: dict) -> dict:
        return {
            k: v for k, v in local_params.items() if k != 'self'
        }
