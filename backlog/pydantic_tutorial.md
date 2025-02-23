# **Szkolenie: Pydantic – Walidacja Danych w Pythonie**

## **1. Wprowadzenie do Pydantic**
Pydantic to biblioteka w Pythonie służąca do **walidacji i serializacji danych** na podstawie typów danych podanych w modelach Pythona. Jest szeroko stosowana w aplikacjach FastAPI i innych projektach wymagających **silnej walidacji danych**.

### **Dlaczego warto używać Pydantic?**
✅ Prosta i czytelna składnia
✅ Automatyczna konwersja typów
✅ Obsługa domyślnych wartości
✅ Możliwość definiowania niestandardowych walidatorów
✅ Szybkie działanie dzięki wykorzystaniu mechanizmu Cython

## **2. Instalacja**
Aby rozpocząć pracę, należy zainstalować bibliotekę Pydantic:
```bash
pip install pydantic
```
Dla wersji Pydantic v2 można użyć:
```bash
pip install pydantic[dotenv]
```

## **3. Tworzenie Modeli**
Podstawowym elementem Pydantic są **modele** dziedziczące po `BaseModel`.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
```

### **Tworzenie obiektu i walidacja danych**
```python
user = User(id=1, name="Jan Kowalski", age=30, email="jan@example.com")
print(user)
```

📌 **Jeśli przekażemy błędne dane, Pydantic automatycznie zwróci błąd.**
```python
user = User(id="abc", name=123, age="trzydzieści", email="janatexample.com")
```
Błąd:
```
ValidationError: 4 validation errors for User
id
  value is not a valid integer
...
```

## **4. Obsługa Domyślnych Wartości**
Jeśli nie podamy wartości dla pola, można ustawić wartość domyślną:
```python
class User(BaseModel):
    id: int
    name: str
    age: int = 18  # Domyślnie 18 lat
```

## **5. Konwersja Typów**
Pydantic automatycznie konwertuje dane do określonych typów:
```python
user = User(id="10", name="Anna", age="25")
print(user)
```
📌 **Dane zostaną automatycznie przekonwertowane:** `id` i `age` zostaną zamienione na liczby całkowite.

## **6. Niestandardowe Walidatory**
Możemy definiować własne walidatory za pomocą dekoratora `@field_validator` (Pydantic v2) lub `@validator` (Pydantic v1):
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int
    
    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Użytkownik musi mieć co najmniej 18 lat")
        return value
```
📌 **Teraz próba utworzenia użytkownika z wiekiem <18 zwróci błąd.**

## **7. Walidacja Formatu (E-mail, URL, UUID)**
Pydantic ma wbudowane klasy do walidacji popularnych formatów:
```python
from pydantic import EmailStr, HttpUrl, UUID4

class User(BaseModel):
    email: EmailStr
    website: HttpUrl
    user_id: UUID4
```
Przykładowe użycie:
```python
user = User(email="test@example.com", website="https://example.com", user_id="550e8400-e29b-41d4-a716-446655440000")
```

## **8. Praca z listami i słownikami**
Możemy tworzyć listy i słowniki jako pola w modelach:
```python
class Order(BaseModel):
    items: list[str]
    prices: dict[str, float]
```
Przykładowe użycie:
```python
order = Order(items=["Apple", "Banana"], prices={"Apple": 1.2, "Banana": 0.8})
```

## **9. Parsowanie JSON i Serializacja**
Pydantic pozwala łatwo konwertować modele na JSON i odwrotnie:
```python
user_json = user.model_dump_json()
print(user_json)

# Załaduj dane z JSON
user2 = User.model_validate_json(user_json)
```

## **10. Konfiguracja Modeli**
Za pomocą klasy `Config` można dostosować zachowanie modelu:
```python
class User(BaseModel):
    name: str
    age: int
    
    class Config:
        validate_assignment = True
```
📌 **Pozwala na walidację przy każdej zmianie wartości atrybutów.**

## **11. Pydantic z FastAPI**
Pydantic jest podstawą walidacji w **FastAPI**:
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item received", "item": item}
```
📌 **FastAPI automatycznie sprawdzi poprawność danych wejściowych!**

## **12. Podsumowanie**
✅ **Automatyczna walidacja danych**
✅ **Obsługa domyślnych wartości i konwersji typów**
✅ **Łatwa integracja z FastAPI**
✅ **Obsługa JSON i serializacji**
✅ **Wsparcie dla list, słowników i formatów (Email, URL, UUID)**

📌 **Pydantic to potężne narzędzie, które ułatwia pracę z danymi i zwiększa bezpieczeństwo aplikacji.** 🚀

