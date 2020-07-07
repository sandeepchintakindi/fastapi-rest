from pydantic import BaseModel


class AuthInput(BaseModel):
    id: str
    password: str
    email: str