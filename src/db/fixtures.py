import asyncio
from datetime import datetime
from src.db.config import AsyncSessionLocal
from src.repositories.customers import CustomerRepository
from src.repositories.products import ProductRepository
from src.repositories.orders import OrderRepository
from src.repositories.order_items import OrderItemRepository

customers = [
    {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
    {"name": "Bob Smith", "email": "bob.smith@example.com"},
    {"name": "Charlie Brown", "email": "charlie.brown@example.com"},
    {"name": "Diana Prince", "email": "diana.prince@example.com"},
    {"name": "Ethan Hunt", "email": "ethan.hunt@example.com"},
    {"name": "Fiona Gallagher", "email": "fiona.gallagher@example.com"},
    {"name": "George Miller", "email": "george.miller@example.com"},
]

products = [
    {"name": "Laptop Pro 15", "price": 1299.99},
    {"name": "Wireless Mouse", "price": 35.50},
    {"name": "Mechanical Keyboard", "price": 120.00},
    {"name": "4K Monitor", "price": 450.00},
    {"name": "Noise-Cancelling Headphones", "price": 199.99},
    {"name": "Smartphone X", "price": 899.00},
    {"name": "Gaming Chair", "price": 320.00},
    {"name": "External SSD 1TB", "price": 150.00},
    {"name": "Webcam HD", "price": 80.00},
    {"name": "Desk Lamp LED", "price": 40.00},
]

orders = [
    {"user_id": 1, "created_at": datetime(2024, 1, 15, 10, 30)},  # Alice
    {"user_id": 1, "created_at": datetime(2024, 3, 2, 14, 45)},   # Alice
    {"user_id": 2, "created_at": datetime(2024, 2, 20, 9, 10)},   # Bob
    {"user_id": 3, "created_at": datetime(2024, 4, 5, 17, 20)},   # Charlie
    {"user_id": 4, "created_at": datetime(2024, 6, 18, 11, 5)},   # Diana
    {"user_id": 5, "created_at": datetime(2024, 7, 1, 19, 40)},   # Ethan
    {"user_id": 6, "created_at": datetime(2024, 8, 22, 16, 0)},   # Fiona
    {"user_id": 7, "created_at": datetime(2024, 9, 10, 13, 25)}  # George
]

order_items = [
    {"order_id": 1, "product_id": 1, "quantity": 1},  # Alice — Laptop
    {"order_id": 1, "product_id": 2, "quantity": 2},  # + 2 мышки
    {"order_id": 2, "product_id": 5, "quantity": 1},  # Alice — наушники
    {"order_id": 3, "product_id": 6, "quantity": 1},  # Bob — телефон
    {"order_id": 3, "product_id": 2, "quantity": 1},  # + мышка
    {"order_id": 3, "product_id": 3, "quantity": 1},  # Charlie — клавиатура
    {"order_id": 6, "product_id": 4, "quantity": 2},  # + 2 монитора
    {"order_id": 5, "product_id": 7, "quantity": 1},  # Diana — кресло
    {"order_id": 6, "product_id": 8, "quantity": 2},  # Ethan — SSD x2
    {"order_id": 6, "product_id": 10, "quantity": 1}, # + лампа
    {"order_id": 7, "product_id": 6, "quantity": 1},  # Fiona — смартфон
    {"order_id": 7, "product_id": 5, "quantity": 1},  # + наушники
    {"order_id": 1, "product_id": 9, "quantity": 1},  # George — вебкамера
]

async def seed():
    async with AsyncSessionLocal() as session:
        await CustomerRepository(session).create_many(customers)
        await ProductRepository(session).create_many(products)
        await OrderRepository(session).create_many(orders)
        await OrderItemRepository(session).create_many(order_items)


if __name__ == "__main__":
    asyncio.run(seed())
