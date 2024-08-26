
# hello.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/api/v1')

@router.get("/")
def hello(message: str):
    return {"message": "Hello {0} !!!".format(message)}

