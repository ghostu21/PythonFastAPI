from fastapi import APIRouter, HTTPException, Query,Path
from typing import List
from datetime import datetime
from pydantic import BaseModel
from models.order_model import OrderModel
from models.users_model import UserModel
from models.product_model import ProductModel
from schemas.users_schema import UserCreateSchema
from config.db import orders_collection,users_collection,products_collection
from schemas.pagination_schema import PaginationParams
from DTO.CreateOrderRequest import OrderCreateRequest
from bson import ObjectId

router=APIRouter()


@router.post("/users/", response_model=UserModel)
async def create_user(user: UserCreateSchema):


    new_user = user.dict()
    inserted_user = users_collection.insert_one(new_user)

    new_user["_id"] = str(inserted_user.inserted_id)

    return UserModel(**new_user)


@router.get("/user-orders/{user_id}", response_model=List[OrderModel])
def get_user_orders(user_id: str, pagination: PaginationParams):
    skip = pagination.offset
    
    orders = orders_collection.find({"userId": user_id}).skip(skip).limit(pagination.limit)

    order_list = [OrderModel(**order) for order in orders]
    
    return order_list

@router.get("/orders/{order_id}", response_model=OrderModel)
def get_order_by_id(order_id: str = Path(..., description="The ID of the order to retrieve")):
    order = orders_collection.find_one({"orderId": order_id})
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return order

@router.get("/products/", response_model=list[ProductModel])
def list_all_products():
    products = list(products_collection.find())
    
    if not products:
        raise HTTPException(status_code=404, detail="No products available")
    
    return products


@router.post("/orders/{user_id}", response_model=OrderModel)
def create_order(user_id: str, order: OrderCreateRequest):
   
    order_data = {
        "orderId": str(ObjectId()), 
        "userId": user_id,
        "timestamp": order.timestamp,
        "items": [{"productId": item.productId, "boughtQuantity": item.boughtQuantity} for item in order.items],
        "totalAmount": order.totalAmount, 
        "userAddress": order.userAddress.dict(),
    }

    inserted_order = orders_collection.insert_one(order_data)

    return OrderModel(**order_data)


