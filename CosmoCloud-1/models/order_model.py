from pydantic import BaseModel

class OrderModel(BaseModel):
    orderId: str
    productId: str
    userId: str
    quantity: int
    time: str
    totalAmount:float