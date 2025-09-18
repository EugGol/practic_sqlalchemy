from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased, joinedload
from src.exceptions import ObjectNotFound
from src.models.models import Customers, OrderItems, Orders, Products
from src.repositories.base import BaseRepository
from src.shemas.schemas import OrderOutWithProducts


class OrderRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model=Orders):
        super().__init__(session, model)

    async def get_orders_with_customer(self):
        cust = aliased(Customers)
        stmt = (
            select(Orders)
            .join(cust, Orders.user_id == cust.id)
            .options(joinedload(Orders.customers))
            .order_by(cust.name)
        )
        return await self.session.execute(stmt).unique().scalars().all()

    async def get_order_with_products_name(self, id: int):
        stmt = (
            select(
                Customers.name,
                Orders.id,
                Orders.created_at,
                func.json_agg(
                    func.json_build_object(
                        "product", Products.name, "qty", OrderItems.quantity
                    )
                ).label("products"),
            )
            .join(OrderItems, Orders.id == OrderItems.order_id)
            .join(Products, OrderItems.product_id == Products.id)
            .join(Customers, Orders.user_id == Customers.id)
            .group_by(Customers.name, Orders.id, Orders.created_at)
            .filter(Orders.id == id)
        )
        try:
            result = await self.session.execute(stmt)
            row = result.mappings().one()
        except NoResultFound as ex:
            raise ObjectNotFound from ex
        return OrderOutWithProducts.model_validate(row)
