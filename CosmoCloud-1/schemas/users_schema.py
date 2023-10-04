# user_schema.py
from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name: str
    email: str
    mobile: str
    password: str



