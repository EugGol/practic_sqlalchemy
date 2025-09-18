from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)

    class Config:
        orm_mode = True


class Customer(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: int
    user_id: int
    created_at: datetime | None = None

    class Config:
        orm_mode = True


class OrderRequestAdd(BaseModel):
    user_id: int
    created_at: datetime | None = None
    products_ids: list[int]


class OrderRequestUpdate(BaseModel):
    user_id: int
    created_at: datetime | None = None


class OrderItemRequestUpdate(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class OrderItem(OrderItemRequestUpdate):
    id: int

    class Config:
        orm_mode = True

class ProductItem(BaseModel):
    product: str
    qty: int

    
class OrderOutWithProducts(BaseModel):
    id: int
    name: str
    created_at: datetime
    products: list[ProductItem]