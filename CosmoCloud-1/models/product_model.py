from pydantic import BaseModel

class ProductModel(BaseModel):
    productId: str
    productName: str
    quantity: int