from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


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


@app.get("/")
def root():
    return {"message": "hello"}
