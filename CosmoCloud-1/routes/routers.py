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

# @app.post("/users/", response_model=UserModel)
# async def create_user(user: UserCreateSchema):
#     # You can implement user creation logic here
#     # For example, insert the user data into the database
#     # Make sure to hash the password securely before storing it

#     # For demonstration purposes, let's create a dummy user
#     new_user = UserModel(**user.dict(), userId=str(len(users) + 1))
#     users.append(new_user)
    
#     return new_user



@router.post("/users/", response_model=UserModel)
async def create_user(user: UserCreateSchema):
    # You can implement user creation logic here
    # For example, insert the user data into the MongoDB collection
    # Make sure to hash the password securely before storing it

    # Create a new user document in the MongoDB collection
    new_user = user.dict()
    inserted_user = users_collection.insert_one(new_user)

    # Add the generated ObjectId to the user dictionary
    new_user["_id"] = str(inserted_user.inserted_id)

    return UserModel(**new_user)


@router.get("/user-orders/{user_id}", response_model=List[OrderModel])
def get_user_orders(user_id: str, pagination: PaginationParams):
    # Calculate skip based on offset
    skip = pagination.offset
    
    # Find orders for the user with limit and skip (offset) for pagination
    orders = orders_collection.find({"userId": user_id}).skip(skip).limit(pagination.limit)
    
    # Convert MongoDB cursor to a list of OrderModel objects
    order_list = [OrderModel(**order) for order in orders]
    
    return order_list

@router.get("/orders/{order_id}", response_model=OrderModel)
def get_order_by_id(order_id: str = Path(..., description="The ID of the order to retrieve")):
    # Find the order by orderId in the MongoDB collection
    order = orders_collection.find_one({"orderId": order_id})
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return order

@router.get("/products/", response_model=list[ProductModel])
def list_all_products():
    # Retrieve all available products from the MongoDB collection
    products = list(products_collection.find())
    
    if not products:
        raise HTTPException(status_code=404, detail="No products available")
    
    return products


@router.post("/orders/{user_id}", response_model=OrderModel)
def create_order(user_id: str, order: OrderCreateRequest):
    # Convert OrderCreateRequest to a dictionary
    order_data = {
        "orderId": str(ObjectId()),  # You can use a better way to generate order IDs
        "userId": user_id,
        "timestamp": order.timestamp,
        "items": [{"productId": item.productId, "boughtQuantity": item.boughtQuantity} for item in order.items],
        "totalAmount": order.totalAmount,  # Total amount at the order level
        "userAddress": order.userAddress.dict(),
    }

    inserted_order = orders_collection.insert_one(order_data)

    return OrderModel(**order_data)


