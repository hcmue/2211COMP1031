from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from typing import Union
from passlib.context import CryptContext
from .db.database import Base, SessionLocal, engine
from .db.models import User
from .models.schema import UserCreate, UserLogin

Base.metadata.create_all(bind=engine)

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "e1e185fd071396f663de65a965384dadec37df0acb3b234ce0b047bd7f85d600"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password_clear_text):
    return pwd_context.hash(password_clear_text)


# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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

##############################


@app.get("/users")
def get_all_user():
    session = SessionLocal()
    users = session.query(User).all()
    return users  # Nen tra ve ViewModel


@app.get("/users/{id}")
def get_user_by_id(id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == id).one_or_none()
    if user:
        return user  # Nen tra ve ViewModel
    else:
        raise HTTPException(status_code=404, detail="Not found")


@app.post("/users")
def create_new_user(model: UserCreate):
    new_user = User(
        username=model.username,
        email=model.email,
        hashed_password=get_password_hash(model.password)
    )
    session = SessionLocal()
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user  # Nen tra ve ViewModel


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
def authenticate(model: UserLogin):
    # Check user có hay ko?
    session = SessionLocal()
    user = session.query(User)\
        .filter(User.username == model.username).one_or_none()
    if user and verify_password(model.password, user.hashed_password):
        # Sinh token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={
                "sub": user.username,
                "email": user.email,
                "roles": ["Admin"]
            },
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorize")

##############################


class TodoItem(BaseModel):
    id: str
    item: str


@app.get("/todos", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


@app.get("/todos/{id}", tags=["todos"])
async def get_todo(id):
    for item in todos:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail=f"not found {id}")


async def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

        return {"username": username}  # Tu lay thong tin user tu db
    except JWTError:
        raise credentials_exception


@app.post("/todos", tags=["todos"])
async def add_todo(todo: TodoItem, current_user: User = Depends(verify_token)) -> dict:
    if current_user:
        todos.append(todo)
        return {
            "data": {"Todo added."}
        }


@app.put("/todos/{id}", tags=["todos"])
async def update_todo(id: int, body: TodoItem) -> dict:
    print(body, body.item, body.id)
    for todo in todos:
        print(todo)
        print(todo["id"], id)
        if int(todo["id"]) == id:
            todo["item"] = body.item
            return {
                "data": f"Todo with id {id} has been updated."
            }

    return {
        "data": f"Todo with id {id} not found."
    }


@app.delete("/todos/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    raise HTTPException(
        status_code=404,
        detail=f"Todo with id {id} not found."
    )


@app.get("/")
def root():
    return {"message": "Hello"}
