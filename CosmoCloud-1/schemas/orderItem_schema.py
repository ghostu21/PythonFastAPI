from pydantic import BaseModel
from typing import List

class OrderItemSchema(BaseModel):
    productId: str
    boughtQuantity: int