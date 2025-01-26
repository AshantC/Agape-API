from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import datetime

class ClientDetails(BaseModel):
    name : str
    email : str
    phone_1: str
    phone_2 : Optional[str] = None
    address : str
    description: str
    price: float
    is_completed : bool = False
    is_deleted : bool = False
    creation: str = datetime.now()
    updated_at: str = datetime.now()
    
# class Product(BaseModel):
#     product_id : str
#     name : str
#     size: str
#     price : float
#     in_stock : bool