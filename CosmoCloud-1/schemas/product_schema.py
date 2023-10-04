from pydantic import BaseModel

class ProductCreateSchema(BaseModel):
    productName: str
    quantity: int

class ProductSchema(ProductCreateSchema):
    productId: str
