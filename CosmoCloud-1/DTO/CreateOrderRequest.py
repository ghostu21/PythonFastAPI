from pydantic import BaseModel
from typing import List

from schemas.orderItem_schema import OrderItemSchema
from schemas.address_schema import UserAddressSchema
from datetime import datetime


class OrderCreateRequest(BaseModel):
    timestamp: datetime
    items: List[OrderItemSchema]
    totalAmount: float
    userAddress: UserAddressSchema  