from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import OrderItems
from src.repositories.base import BaseRepository


class OrderItemRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model=OrderItems):
        super().__init__(session, model)
