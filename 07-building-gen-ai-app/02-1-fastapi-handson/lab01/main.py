# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello world"}

@app.get("/")
def home():
    return {"message": "Hello"}


@app.get("/items/{item_id}")
async def read_item(item_id):
 return {"item_id": item_id}
