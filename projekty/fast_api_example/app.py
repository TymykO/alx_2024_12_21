# pip install fastapi

from fastapi import FastAPI, Depends

from db_adapters import DbAdapter, InMemoryDbAdapter
from schemas import Item


app = FastAPI()


def get_db_adapter() -> DbAdapter:
    return InMemoryDbAdapter()


@app.get("/")
def root():
    return {"message": "Hello FastAPI!"}

@app.get("/items/{item_id}")
def get_item(item_id: int, db: DbAdapter = Depends(get_db_adapter)) -> Item:
    return db.get_item(item_id)


@app.get("/items")
def items_list(db: DbAdapter = Depends(get_db_adapter)) -> list[Item]:
    return db.get_items()

@app.post("/items/")
def create_item(item: Item, db: DbAdapter = Depends(get_db_adapter)) -> Item:
    return db.create_item(item)


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, db: DbAdapter = Depends(get_db_adapter)) -> Item:
    return db.update_item(item_id, item)


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: DbAdapter = Depends(get_db_adapter)) -> None:
    return db.delete_item(item_id)

# uvicorn app:app