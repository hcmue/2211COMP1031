from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def abc():
    return "Hello"
