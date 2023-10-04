# address_model.py
from pydantic import BaseModel

class AddressModel(BaseModel):
    orderId: str
    country: str
    city: str
    zipcode: str
