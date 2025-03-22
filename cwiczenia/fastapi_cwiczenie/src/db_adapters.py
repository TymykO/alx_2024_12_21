from abc import ABC, abstractmethod
from typing import Optional
from src.schemas import Product
import json

class IDbAdapter(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def product_list(self) -> list[Product]:
        pass

    @abstractmethod
    def update_product(self, product_id: int, product: Product):
        pass

    @abstractmethod
    def delete_product(self, product_id: int):
        pass

class InMemoryDbAdapter(IDbAdapter):
    def __init__(self, db: Optional[dict] = None):
        if db is None:
            db = {}
        self.db = db

    def add_product(self, product: Product):
        self.db[product.id] = product.model_dump()

    def get_product(self, product_id: int) -> Product:
        return Product(**self.db[product_id])  

    def product_list(self) -> list[Product]:
        return [Product(**product) for product in self.db]

    def update_product(self, product_id: int, product: Product):
        self.db[product_id] = product.model_dump()

    def delete_product(self, product_id: int):
        del self.db[product_id]


class JsonFileDbAdapter(IDbAdapter):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.db = self._load_db()

    def _load_db(self) -> list[Product]:
        with open(self.file_path, "r") as f:
            return [Product(**json.loads(line)) for line in f]

    def _save_db(self):
        with open(self.file_path, "w") as f:
            json.dump([product.model_dump() for product in self.db], f)

    def add_product(self, product: Product):
        self.db.append(product)
        self._save_db()

    def get_product(self, product_id: int) -> Product:
        return next((product for product in self.db if product.id == product_id), None)

    def product_list(self) -> list[Product]:
        return self.db

    def update_product(self, product_id: int, product: Product):
        self.db[product_id] = product.model_dump()
        self._save_db()

    def delete_product(self, product_id: int):
        self.db = [product for product in self.db if product.id != product_id]
        self._save_db()
    