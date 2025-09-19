from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.analytics import AnalyticsRepository
from src.repositories.customers import CustomerRepository
from src.repositories.orders import OrderRepository
from src.repositories.order_items import OrderItemRepository
from src.repositories.products import ProductRepository


class UnitOfWork(Protocol):
    session: AsyncSession
    customer: CustomerRepository
    order: OrderRepository
    order_item: OrderItemRepository
    product: ProductRepository
    analytics: AnalyticsRepository
