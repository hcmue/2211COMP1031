# FastAPI

### Tham khảo: https://testdriven.io/blog/fastapi-react/

## Tạo virtual environment

- Tạo: `$python -m venv venv`
- Active virtual env (Wins): `$venv\Scripts\activate`
- Xuất file thư viện dùng trong project:
  Đứng ngay virtual environment:
  ```
  $pip freeze > requirements.txt
  ```
- Dựng lại environment của project:
  - Tạo virtual environment
  - Chạy lệnh cài các packages trong file requirements.txt
  ```
  $ pip install -r requirements.txt
  ```

# SQLAlchemy

## Cài thư viện

```
pip install sqlalchemy
pip install pymysql
```

- Tham khảo sqlalchemy + pymysql
  https://hackersandslackers.com/python-database-management-sqlalchemy/
