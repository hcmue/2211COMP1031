## Tạo virtual environment

- Tạo: `$python -m venv venv`
- Activate virtual env (Wins): `$venv\Scripts\activate`
- Xuất file thư viện dùng trong project:
  Đứng ngay virtual environment:
  ```
  $pip freeze > requirements.txt
  ```
- Dựng lại environment của project:
  - Tạo virtual environment
  - Activate virtual environment vừa tạo
  - Chạy lệnh cài các packages trong file requirements.txt
  ```
  $ pip install -r requirements.txt
  ```

## Tham khảo: https://testdriven.io/blog/fastapi-react/

## Cấu trúc thư mục frontend

```
backend
|__venv
|__main.py <--- chạy $python main.py
|__app
     |__ __init__.py <-- đánh dấu TM app là module
     |__ myapi.py (trong đó có chứa biến app = FastAPI()
```

## Authentication using password and Bearer Token

https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt

Install `python-jose` to generate and verify the JWT tokens

```
pip install "python-jose[cryptography]"
```

Install `passlib` to encrypt and decrypt.

```
pip install "passlib[bcrypt]"
```
