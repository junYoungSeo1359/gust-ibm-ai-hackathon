from pydantic import BaseModel
from typing import List


class Item(BaseModel):
  id: int
  item : str

class Items(BaseModel):
  todos : List[Item]


class Product(BaseModel):
  id: int
  product_name : str

  
class Products(BaseModel):
  todos : List[Product]
