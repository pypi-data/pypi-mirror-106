from pydantic import BaseModel


class AccGetInfo(BaseModel):
    id: int
    type: int
    domain: str
    verified: int
    first_name: str
    last_name: str
    register_date: int
    balance: int
