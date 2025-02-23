# **Szkolenie: FastAPI – Tworzenie API w Pythonie**

## **1. Wprowadzenie do FastAPI**
FastAPI to nowoczesny framework do budowy API w Pythonie, który cechuje się:
✅ Szybkością porównywalną do NodeJS i Go 🚀
✅ Automatyczną dokumentacją OpenAPI 📜
✅ Obsługą walidacji danych dzięki Pydantic 🛠️
✅ Asynchroniczną obsługą żądań (async/await) ⚡

## **2. Instalacja**
Aby zainstalować FastAPI i serwer ASGI (np. Uvicorn), użyj:
```bash
pip install fastapi uvicorn
```

## **3. Tworzenie Pierwszego API**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Witaj w FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```
Uruchom serwer za pomocą:
```bash
uvicorn main:app --reload
```
Serwer uruchomi się pod adresem: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## **4. Automatyczna Dokumentacja API**
FastAPI generuje dokumentację automatycznie:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## **5. Obsługa Metod HTTP**
FastAPI obsługuje standardowe metody HTTP:
```python
@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    return {"item_id": item_id, "name": name}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```

## **6. Walidacja Danych z Pydantic**
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

## **7. Asynchroniczne API**
FastAPI obsługuje asynchroniczne żądania dzięki `async def`:
```python
import asyncio

@app.get("/slow-task")
async def slow_task():
    await asyncio.sleep(5)
    return {"message": "Task completed!"}
```

## **8. Middleware i Obsługa Błędów**
FastAPI umożliwia dodanie middleware do globalnej obsługi błędów:
```python
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
def global_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"error": "Internal Server Error"})
```

## **9. Autoryzacja i Uwierzytelnianie**
FastAPI obsługuje uwierzytelnianie JWT i OAuth2:
```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/protected/")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

## **10. Podsumowanie**
✅ **Łatwość tworzenia API**  
✅ **Automatyczna dokumentacja**  
✅ **Wsparcie dla walidacji, autoryzacji i middleware**  
✅ **Obsługa asynchronicznych operacji**  

📌 **FastAPI to idealne rozwiązanie do budowy nowoczesnych API w Pythonie!** 🚀

