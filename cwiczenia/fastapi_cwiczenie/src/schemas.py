from pydantic import BaseModel
from decimal import Decimal

class Product(BaseModel):
    name: str
    price: Decimal
    
    model_config = {
        "json_encoders": {
            Decimal: lambda x: str(x)
        }
    }
