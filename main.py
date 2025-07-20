from fastapi import FastAPI
from routes.product_routes import router as product_router
from routes.order_routes import router as order_router

app = FastAPI(
    title="HROne Backend Intern Task",
    description="E-commerce API with FastAPI and MongoDB",
    version="1.0.0"
)

# Include routes
app.include_router(product_router)
app.include_router(order_router)
