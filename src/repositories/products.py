from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.exceptions import ProductNotFound
from src.models.models import OrderItems, Products
from src.repositories.base import BaseRepository


class ProductRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model=Products):
        super().__init__(session, model)


    async def get_top_products(self):
        stmt = (
            select(
                Products.name,
                Products.price,
                func.sum(OrderItems.quantity)
                .label("total_quantity")  
            )
            .join(OrderItems, Products.id == OrderItems.product_id)
            .group_by(Products.name, Products.price)
            .order_by(func.sum(OrderItems.quantity).desc())
            .limit(3)
        )
        result = await self.session.execute(stmt)
        return result.all()
    

    async def count_by_ids(self, product_ids: list[int]):
        stmt = select(func.count(Products.id)).where(Products.id.in_(product_ids))
        result = await self.session.execute(stmt)
        count_products = result.scalar()
        if count_products != len(product_ids):
            raise ProductNotFound
