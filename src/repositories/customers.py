from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.exceptions import UserNotFound
from src.models.models import Customers, Orders
from src.repositories.base import BaseRepository


class CustomerRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model=Customers):
        super().__init__(session, model)

    async def get_customers_with_orders(self):
        stmt = select(Customers).options(joinedload(Customers.orders))
        return await self.session.execute(stmt).unique().scalars().all()

    async def get_count_orders_by_customer(self):
        stmt = (
            select(Customers.name, func.count(Orders.id))
            .join(Orders, Customers.id == Orders.user_id)
            .group_by(Customers.name)
            .order_by(func.count(Orders.id).desc())
        )
        return await self.session.execute(stmt).all()
    
    async def customer_exist(self, id: int):
        stmt = select(Customers).where(Customers.id == id)
        result = await self.session.execute(stmt).scalar().one_or_none()
        if result:
            return True
        raise UserNotFound
