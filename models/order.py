from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    productId: str  # must match exactly as per request body
    qty: int


class OrderModel(BaseModel):
    userId: str  # must match exactly as per request body
    items: List[OrderItem]

    class Config:
        schema_extra = {
            "example": {
                "userId": "user_1",
                "items": [
                    { "productId": "123456789", "qty": 2 },
                    { "productId": "22222222", "qty": 1 }
                ]
            }
        }
