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

## Cấu trúc thư mục frontend

```
backend
|__venv
|__main.py <--- chạy $python main.py
|__app
     |__ __init__.py <-- đánh dấu TM app là module
     |__ myapi.py (trong đó có chứa biến app = FastAPI()
```
