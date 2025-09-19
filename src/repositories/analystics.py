from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.models import OrderItems, Orders, Products
from src.repositories.base import BaseRepository
from src.shemas.analystics import TopProductsOut

class AnalysticsRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model=None):
        super().__init__(session, model)

    async def get_top_products_by_period(self, start_dt, end_dt):
        stmt = (
            select(
                Products.id.label("product_id"),
                Products.name.label("product_name"),
                Products.price,
                func.sum(OrderItems.quantity)
                .label("ordered_quantity")  
            )
            .join(OrderItems, Products.id == OrderItems.product_id)
            .join(Orders, OrderItems.order_id == Orders.id)
            .group_by(Products.name, Products.price, Products.id)
            .order_by(func.sum(OrderItems.quantity).desc())
            .where(Orders.created_at.between(start_dt, end_dt))
            .limit(3)
        )
        query = await self.session.execute(stmt)
        result = query.mappings().all()
        return [TopProductsOut.model_validate(row) for row in result]