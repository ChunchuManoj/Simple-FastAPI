from pydantic import BaseModel, Field
from typing import List


class ProductSize(BaseModel):
    size: str
    quantity: int


class ProductModel(BaseModel):
    name: str
    price: float
    sizes: List[ProductSize]

    class Config:
        schema_extra = {
            "example": {
                "name": "Cotton T-Shirt",
                "price": 499.99,
                "sizes": [
                    { "size": "small", "quantity": 10 },
                    { "size": "large", "quantity": 5 }
                ]
            }
        }
