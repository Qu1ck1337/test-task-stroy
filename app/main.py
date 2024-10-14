from fastapi import FastAPI

from app.database import Base, engine
from app.routers import products, categories

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
app.include_router(categories.router)