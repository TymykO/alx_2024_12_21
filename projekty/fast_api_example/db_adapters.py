from fastapi import HTTPException

from abc import ABC, abstractmethod

from schemas import Item

from db import database

class DbAdapter(ABC):
    @abstractmethod
    def get_item(self, item_id: int) -> Item:
        pass
    
    @abstractmethod
    def create_item(self, item: Item) -> Item:
        pass
    
    @abstractmethod
    def update_item(self, item_id: int, item: Item) -> Item:
        pass       

    @abstractmethod
    def delete_item(self, item_id: int) -> None:
        pass
        
    @abstractmethod
    def get_items(self) -> list[Item]:
        pass

class InMemoryDbAdapter(DbAdapter):
    def get_item(self, item_id: int) -> Item:
        if len(database) < item_id:
            raise HTTPException(status_code=404, detail="Item not found")

        return Item(**database[item_id - 1]) 
    
    def create_item(self, item: Item) -> Item:
        database.append(item.model_dump())
        return item
    
    def update_item(self, item_id: int, item: Item) -> Item:
        database[item_id - 1] = item.model_dump()
        return item
    
    def delete_item(self, item_id: int) -> None:
        if len(database) < item_id:
            raise HTTPException(status_code=404, detail="Item not found")
        database.pop(item_id - 1)

    def get_items(self) -> list[Item]:
        return [Item(**item) for item in database]
