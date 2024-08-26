
# main.py

from fastapi import FastAPI
from routers import hello

app = FastAPI()

# Add router
app.include_router(hello.router)

