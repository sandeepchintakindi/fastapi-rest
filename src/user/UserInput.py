from pydantic import BaseModel


class UserInput(BaseModel):
    id: str
    name: str
    email: str