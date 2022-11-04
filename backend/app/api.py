import re

from requests import session
from .DbUtil import DbUtil
import pymysql
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .db.database import Base, SessionLocal, engine
from .db.schema import User

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho tất cả các trang đều access API được
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/users")
def get_all_users():
    session = SessionLocal()
    users = session.query(User).all()
    return users  # Convert ViewModel


@app.get("/users/{id}")
def get_user(id: int):
    session = SessionLocal()
    user = session.query(User)\
        .filter(User.id == id).one_or_none()
    if user:
        return user  # Convert ViewModel
    else:
        raise HTTPException(
            status_code=404, detail="Not found"
        )


todos = [
    {
        "id": 1,
        "item": "Read a book."
    },
    {
        "id": 2,
        "item": "Cycle around town."
    }
]


@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


@app.get("/todo/{id}", tags=["todos"])
async def get_todos(id: int) -> dict:
    for item in todos:
        print(item)
        if item["id"] == id:
            return {"data": item}
    raise HTTPException(status_code=404, detail=f"Item {id} not found")


class TodoItem(BaseModel):
    id: int
    item: str


@app.post("/todo", tags=["todos"])
async def add_todo(todo: TodoItem) -> dict:
    for item in todos:
        print(item)
        if item["id"] == todo.id:
            raise HTTPException(
                status_code=400, detail=f"Item {todo.id} existed")
    todos.append(todo)
    return {
        "data": {"Todo added."}
    }


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: TodoItem) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body.item
            return {
                "data": f"Todo with id {id} has been updated."
            }

    raise HTTPException(status_code=404, detail=f"Item {id} not found")


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    raise HTTPException(status_code=404, detail=f"Item {id} not found")


@app.get("/")
def root():
    return {"message": "hello"}


@app.get("/loai")
def get_all_loai():
    try:
        # Connect to the database
        connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='cnwebcomp103102', cursorclass=pymysql.cursors.DictCursor)
        # Get data
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM loai")
            result = cursor.fetchall()
            ds_loai = []
            for loai in result:
                print(loai)
                ds_loai.append(loai)
            return ds_loai
    except:
        raise HTTPException(status_code=403, detail="Error")


class LoaiModel(BaseModel):
    tenloai: str


@app.post("/loai")
def create_new_loai(model: LoaiModel):
    sqlinsert = f'''
    INSERT INTO loai(tenloai) VALUES('{model.tenloai}')
    '''
    result = DbUtil.insert_and_get_id(sqlinsert)
    if result:
        return {"inserted_id": result}
    else:
        return {"message": "Can not create"}
