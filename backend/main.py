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
