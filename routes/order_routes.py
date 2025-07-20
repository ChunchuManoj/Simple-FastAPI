from fastapi import APIRouter, Path, Query
from models.order import OrderModel
from db.mongodb import order_collection, product_collection
from bson import ObjectId

router = APIRouter()


@router.post("/orders", status_code=201)
def create_order(order: OrderModel):
    order_dict = order.dict()
    result = order_collection.insert_one(order_dict)
    return {"id": str(result.inserted_id)}


@router.get("/orders/{user_id}", status_code=200)
def get_orders_by_user(
    user_id: str = Path(...),
    limit: int = 10,
    offset: int = 0
):
    query = {"userId": user_id}
    cursor = order_collection.find(query).skip(offset).limit(limit)
    orders = []

    for order in cursor:
        enriched_items = []
        for item in order.get("items", []):
            product = product_collection.find_one({"_id": ObjectId(item["productId"])})
            product_details = {
                "name": product["name"],
                "id": str(product["_id"])
            } if product else {}

            enriched_items.append({
                "productDetails": product_details,
                "qty": item["qty"]
            })

        orders.append({
            "id": str(order["_id"]),
            "items": enriched_items,
            "total": order.get("total", 0.0)
        })

    page_info = {
        "next": str(offset + limit),
        "limit": offset,
        "previous": offset - limit
    }

    return {
        "data": orders,
        "page": page_info
    }
