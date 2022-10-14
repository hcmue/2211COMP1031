from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

# Restful API: GET, POST, PUT, DELETE - mỗi loại chỉ làm 1 nhiệm vụ
'''
Cung cấp các API liên quan đến sinh viên:
Method  API endpoint
GET     host/students
GET     host/students/{id}
GET     host/students/search
POST    host/students
PUT     host/students/{id}
DELETE  host/students/{id}
GraphQL là gì?
'''


class Student(BaseModel):
    id: str
    name: str
    gpa: float


@app.get("/students")
def get_students():
    pass


@app.get("/students/{id}")
def get_student(id: str):
    pass


@app.post("/students")
def create_new_students(model: Student):
    pass


@app.put("/students/{id}")
def update_student(id: str, model: Student):
    pass


@app.delete("/students/{id}")
def remove_student(id: str):
    pass


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}


@app.get("/hello")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
