from pydantic import BaseModel


class CallbackGetSettings(BaseModel):
    confirmation_code: str
    is_available: int
    method: int
    secret_key: str
    url: str
    version: int