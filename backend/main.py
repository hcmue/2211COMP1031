import json
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return {
        "message": "Welcome K46 to FastAPI"
    }


@app.get("/hello")
def hello(name):
    return {
        "message": f"Hello {name}"
    }


@app.post("/students")
def create_new_student(id, name, gpa):
    return {
        "id": id,
        "name": name,
        "gpa": gpa
    }


class Student(BaseModel):
    id: str
    name: str
    gpa: float


@app.get("/students")
def get_all_students():
    with open("studentdata.json") as f:
        data = json.load(f)
        return data


@app.get("/students/{id}")
def get_student(id):
    with open("studentdata.json", encoding="utf8") as f:
        data = json.load(f)
        for item in data:
            if item["id"] == id:
                return item
    return None


@app.post("/students")
def create_students(model: Student):
    print(model)
