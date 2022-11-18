import pymysql
from datetime import datetime, timedelta
from typing import Union
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from .models.models import UserRegister, LoginVM
from .DbUtil import DbUtil
from .db.database import Base, SessionLocal, engine
from .db.schema import User

Base.metadata.create_all(bind=engine)

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "339114409fd918b6cc86c09afafc467953c17b468b3800648edb2990fbc518c1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho tất cả các trang đều access API được
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/login")
async def login(model: LoginVM):
    session = SessionLocal()
    # 1. Check valid user/pass
    user = session.query(User)\
        .filter(User.username == model.username)\
        .one_or_none()
    if user and verify_password(model.password, user.password):
        # 2. Generate token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={
                "sub": user.username,
                "name": user.fullname
            },
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.get("/users")
def get_all_users():
    session = SessionLocal()
    users = session.query(User).all()
    return users  # Convert ViewModel


@app.get("/users/{id}")
def get_user(id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == id).one_or_none()
    if user:
        return user  # Convert ViewModel
    else:
        raise HTTPException(
            status_code=404, detail="Not found"
        )


@app.post("/users")
def register(model: UserRegister, token: str = Depends(oauth2_scheme)):
    new_user = User(
        fullname=model.fullname,
        password=get_password_hash(model.password),
        username=model.username
    )
    session = SessionLocal()
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@app.delete("/users/{id}")
def remove_user(id: int):
    session = SessionLocal()
    session.query(User).filter(User.id == id).delete()
    session.commit()


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
