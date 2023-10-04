# address_schema.py
from pydantic import BaseModel

class AddressCreateSchema(BaseModel):
    orderId: str
    country: str
    city: str
    zipcode: str

class AddressSchema(AddressCreateSchema):
    pass


class UserAddressSchema(BaseModel):
    City: str
    Country: str
    ZipCode: str
