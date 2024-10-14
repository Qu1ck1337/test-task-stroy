from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


# Category
class CategoryBase(BaseModel):
    id: int

class CategoryCreate(BaseModel):
    name: str

class Category(CategoryCreate, CategoryBase):
    model_config = ConfigDict(from_attributes = True)


# Product
class ProductBase(BaseModel):
    id: int

class ProductCreate(BaseModel):
    category_id: int
    name: str
    description: Optional[str] = None
    price: float

class ProductUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

    model_config = ConfigDict(from_attributes = True)

class Product(ProductCreate, ProductBase):
    model_config = ConfigDict(from_attributes = True)