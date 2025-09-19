from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.analytics import AnalyticsRepository
from src.repositories.customers import CustomerRepository
from src.repositories.orders import OrderRepository
from src.repositories.order_items import OrderItemRepository
from src.repositories.products import ProductRepository


class SqlAlchemyUoW:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.customer = CustomerRepository(session)
        self.product = ProductRepository(session)
        self.order = OrderRepository(session)
        self.order_item = OrderItemRepository(session)
        self.analytics = AnalyticsRepository(session)
