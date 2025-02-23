from pydantic import BaseModel, EmailStr, HttpUrl, UUID4, field_validator
from typing import List, Dict

# Definicja modelu User
class User(BaseModel):
    id: int
    name: str
    age: int = 18
    email: EmailStr
    website: HttpUrl = "https://example.com"
    user_id: UUID4

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Użytkownik musi mieć co najmniej 18 lat")
        return value

# Tworzenie instancji modelu User
user = User(
    id=1,
    name="Jan Kowalski",
    age=30,
    email="jan@example.com",
    website="https://example.com",
    user_id="550e8400-e29b-41d4-a716-446655440000"
)
print(user)

# Definicja modelu Order
class Order(BaseModel):
    items: List[str]
    prices: Dict[str, float]

# Tworzenie instancji modelu Order
order = Order(
    items=["Apple", "Banana"],
    prices={"Apple": 1.2, "Banana": 0.8}
)
print(order)

# Parsowanie do JSON i z JSON
user_json = user.model_dump_json()
print(user_json)

user2 = User.model_validate_json(user_json)
print(user2)
