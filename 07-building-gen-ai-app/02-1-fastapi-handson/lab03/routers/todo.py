from fastapi import APIRouter, HTTPException, status
from models import Item, Items
todo_router = APIRouter()

todo_list = [] 

@todo_router.get("/items/{item_id}")
async def read_item(item_id: int):
  for item in todo_list:
    print(item)
    if item.id == item_id:
      return item

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="id가 {0} todo가 존재하지 않습니다.".format(item_id)
  )  

@todo_router.get("/items", response_model=Items)
async def read_item_all():
  return {"todos" : todo_list}

@todo_router.post("/items")
async def add_item(item: Item):
  todo_list.append(item)
  return {"message" : "성공적으로 추가되었습니다."}

@todo_router.put("/items/{item_id}") 
async def update_todo(item: Item, item_id: int):
  for todo in todo_list:
    print(item)
    if todo.id == item_id:
      todo.item = item.item
      return {"message" : "성공적으로 업데이트 되었습니다."}

  return {"message" : "{0} todo 가 없습니다.".format(item_id)}

@todo_router.delete("/items/{item_id}")
async def delete_todo(item_id: int):
  for index in range(len(todo_list)):
    todo = todo_list[index]
    if todo.id == item_id:
      todo_list.pop(index)
  
  return {"message" : "id 가 {0}인 todo 가 없습니다.".format(item_id)} 

@todo_router.delete("/items")
async def delete_todo_all():
  todo_list.clear()
  
  return { "message" : "Todos가 삭제되었습니다."}
