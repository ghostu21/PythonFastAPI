from pymongo import MongoClient
from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse
from bson import ObjectId
from pydantic import BaseModel

# MongoDB setup
client = MongoClient("mongodb+srv://mayanklahoti3456:JrspYO2tkZoOs79i@cluster0.kd70wgo.mongodb.net/?retryWrites=true&w=majority")
db = client["cosmoCloud"]


users_collection = db["users"]
addresses_collection = db["addresses"]
products_collection = db["products"]

orders_collection=db["orders"]
