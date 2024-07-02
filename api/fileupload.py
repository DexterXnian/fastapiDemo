from fastapi import APIRouter,UploadFile,Form,HTTPException
import os

api_file = APIRouter()

@api_file.post("")
async def get_file(file: UploadFile):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")
    savepath = os.path.join("upimg",file.filename)
    with open(savepath,"wb") as f:
        for line in file.file:
            f.write(line)
    print("pass")
    return {"file": "get file", "filename": file.filename, "url": f"/files/{file.filename}"}


# from fastapi import FastAPI, File, UploadFile, HTTPException,APIRouter
# from fastapi.responses import FileResponse
# import os
# import shutil

# api_file = APIRouter()

# UPLOAD_DIRECTORY = "./upimg/"

# # 确保上传目录存在
# if not os.path.exists(UPLOAD_DIRECTORY):
#     os.makedirs(UPLOAD_DIRECTORY)

# @api_file.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     if not file:
#         raise HTTPException(status_code=400, detail="No file provided")
    
#     file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
#     with open(file_location, "wb") as f:
#         shutil.copyfileobj(file.file, f)
    
#     return {"filename": file.filename, "url": f"/files/{file.filename}"}

# @api_file.get("/files/{filename}")
# async def get_file(filename: str):
#     file_location = os.path.join(UPLOAD_DIRECTORY, filename)
#     if not os.path.exists(file_location):
#         raise HTTPException(status_code=404, detail="File not found")
    
#     return FileResponse(file_location)
