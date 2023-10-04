from pydantic import BaseModel
from fastapi import  Query

class PaginationParams(BaseModel):
    limit: int = Query(..., description="Number of items to retrieve per page")
    offset: int = Query(0, description="Offset for pagination")
