
# order_schema.py
from pydantic import BaseModel

class OrderCreateSchema(BaseModel):
    productId: str
    userId: str
    quantity: int
    time: str
    totalAmount:float

class OrderSchema(OrderCreateSchema):
    orderId: str
