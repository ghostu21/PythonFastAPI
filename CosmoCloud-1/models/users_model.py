from pydantic import BaseModel

class UserModel(BaseModel):
    userId: str
    name: str
    email: str
    mobile: str
    password: str
