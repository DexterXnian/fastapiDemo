from fastapi import APIRouter
from fastapi import Request

api_book = APIRouter()

@api_book.get("/get")
async def get_book(request:Request):
    get_test = request.query_params
    print(get_test)
    return {"message": "get book"}

@api_book.put("/put")
async def put_book():
    return {"message": "put book"}

@api_book.post("/post")
async def post_book(request:Request,json_data:dict=None):
    post_book = await request.json()
    print(post_book)
    return {"message": "post book"}

@api_book.delete("/delete")
async def delete_book():
    return {"message": "delete book"}