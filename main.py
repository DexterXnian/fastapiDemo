from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models import User
from utils import hash_password, verify_password, create_access_token

from fastapi.staticfiles import StaticFiles

from typing import Union
from fastapi import FastAPI
import uvicorn
from api.book import api_book
from api.fileupload import api_file

app = FastAPI()

# 路由分发
app.include_router(api_book,prefix="/book",tags=["图书接口"])
app.include_router(api_file,prefix="/file",tags=["文件上传"])

app.mount("/upimg", StaticFiles(directory="upimg"), name="upimg")
# get post put delete

# get方法的 根
@app.get("/")
async def get_root():
    return {"message": "get"}


# get方法
@app.post("/hello")
async def post_dd():
    return {"message": "post"}

# get方法
@app.put("/hello")
async def put_dd():
    return {"message": "put"}

# get方法
@app.delete("/hello")
async def put_dd():
    return {"message": "delete"}

if __name__ == "__main__":
    uvicorn.run(app="main:app",host="127.0.0.1", port=8080,reload=True)