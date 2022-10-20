from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Cấu hình CORS cho phép tất cả các nguồn đều truy cập được API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]


@app.get("/todos", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


@app.get("/todos/{id}", tags=["todos"])
async def get_todo(id):
    for item in todos:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail=f"not found {id}")


@app.post("/todos", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": {"Todo added."}
    }


@app.get("/")
def root():
    return {"message": "Hello"}
