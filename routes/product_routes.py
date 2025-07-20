from fastapi import APIRouter, Query
from models.product import ProductModel
from db.mongodb import product_collection
from bson import ObjectId
import re

router = APIRouter()

@router.get("/", status_code=200)
def root():
    return {"message": "Welcome to the HROne Backend API"}

@router.post("/products", status_code=201)
def create_product(product: ProductModel):
    product_dict = product.dict()
    result = product_collection.insert_one(product_dict)
    return {"id": str(result.inserted_id)}


@router.get("/products", status_code=200)
def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = 10,
    offset: int = 0
):
    query = {}

    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}

    if size:
        query["sizes.size"] = size

    cursor = product_collection.find(query).skip(offset).limit(limit)
    products = []

    for doc in cursor:
        products.append({
            "id": str(doc["_id"]),
            "name": doc["name"],
            "price": doc["price"]
        })

    page_info = {
        "next": str(offset + limit),
        "limit": offset,
        "previous": offset - limit
    }

    return {
        "data": products,
        "page": page_info
    }
