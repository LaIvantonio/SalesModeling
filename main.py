from fastapi import FastAPI, UploadFile, Form
from pythonProject.work import main
from typing import List
import pandas as pd
import io

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/api/upload")
async def upload_file(file: UploadFile = Form(...)):
    try:
        # Читаем содержимое файла
        content = await file.read()
        
        # Создаем BytesIO объект, чтобы передать его в pd.read_excel
        file_like = io.BytesIO(content)
        
        # Обрабатываем файл, например, создаем DataFrame
        df = pd.read_excel(file_like)
        
        main(file.filename)
        
        print(f"Загружен файл: {file.filename}")
    except Exception as e:
        print(f"Произошла ошибка при загрузке файла {file.filename}: {str(e)}")
    
    return {"message": "Файл успешно загружен"}
    
    

