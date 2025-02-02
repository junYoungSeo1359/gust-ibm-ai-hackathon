from fastapi import APIRouter, HTTPException, status
from models import Product, Products

product_router = APIRouter()

product_list = [] 

@product_router.get("/products/{product_id}")
async def read_product(product_id: int):
  for product in product_list:
    print(product)
    if product.id == product_id:
      return product

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="id가 {0} product 이  존재하지 않습니다.".format(product_id)
  )  

@product_router.get("/products", response_model=Products)
async def read_product_all() -> dict:

  return {"products" : product_list}

@product_router.post("/products")
async def add_product(product: Product):
  product_list.append(product)
  return {"message" : "성공적으로 추가되었습니다."}

@product_router.put("/products/{product_id}") 
async def update_product(product: Product, product_id: int):
  for prd in product_list:
    print(prd)
    
    if prd.id == product_id:
      prd.product_name = product.product_name
      return {"message" : "성공적으로 업데이트 되었습니다."}

  return {"message" : "{0} product 이 없습니다.".format(product_id)}

@product_router.delete("/products/{product_id}")
async def delete_product(product_id: int):
  for index in range(len(product_list)):
    product = product_list[index]
    
    if product.id == product_id:
      product_list.pop(index)
      
      return {"message" : "id 가 {0}인 product이 삭제되었습니다.".format(product_id)} 
  
  return {"message" : "id 가 {0}인 product이 없습니다.".format(product_id)} 

@product_router.delete("/products")
async def delete_product_all():
  product_list.clear()
  
  return { "message" :  "Products 가 삭제되었습니다."}
