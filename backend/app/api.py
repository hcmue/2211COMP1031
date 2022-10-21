from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho tất cả các trang đều access API được
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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
