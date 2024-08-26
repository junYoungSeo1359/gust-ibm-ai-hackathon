from pydantic import BaseModel
from typing import List

class Product(BaseModel):
  id: int
  product_name : str

  
class Products(BaseModel):
  todos : List[Product]
  