# UCHET KZ

Создать .env файл
```
.env

BACKEND_CORS_ORIGINS=["http://localhost:8000", "https://localhost:8000", "http://localhost", "https://localhost"]
DEBUG=True
SERVER_HOST=http://localhost:8000
SERVER_NAME=uchetkz
```

Установить пакеты

```
pip install -r requirements.txt 
```


Запустить локально
```
python -m uvicorn app.main:app --reload 
```

Swagger
```
http://localhost:8000/docs
```
