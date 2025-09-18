from datetime import date
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, DateTime, func, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.db.config import Base

class Customers(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    created_at: Mapped[date] = mapped_column(DateTime, default=func.now())
    phone: Mapped[str] = mapped_column(String(20), nullable=True)

    orders = relationship("Orders", back_populates="customers")



class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]  = mapped_column(String(100), nullable=False)
    price: Mapped[Decimal]  = mapped_column(Numeric(10, 2), nullable=False)

    items = relationship("OrderItems", back_populates="product")

class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)
    created_at: Mapped[date] = mapped_column(DateTime, default=func.now())

    customers = relationship("Customers", back_populates="orders")
    items = relationship("OrderItems", back_populates="order")

class OrderItems(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)

    order = relationship("Orders", back_populates="items")
    product = relationship("Products", back_populates="items")



