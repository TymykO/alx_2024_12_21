from fastapi import FastAPI, Depends
from src.db_adapters import IDbAdapter, InMemoryDbAdapter
app = FastAPI()

def get_db_adapter() -> IDbAdapter:
    db = [{
        "name": "Product 1",
        "price": 100
    }, {
        
        "name": "Product 2",
        "price": 200
    }]
    return InMemoryDbAdapter(db)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/products")
def get_products(db: IDbAdapter = Depends(get_db_adapter)):
    return db.product_list()





