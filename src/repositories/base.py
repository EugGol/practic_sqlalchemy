
from sqlalchemy import select, insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions import ObjectNotFound



class BaseRepository:

    def __init__(self, session: AsyncSession, model):
        self.model = model
        self.session = session

    async def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def create_many(self, data):
        await self.session.execute(insert(self.model), data)


    async def get_all(self, **kwargs):
        stmt = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_one(self, **kwargs):
        stmt = select(self.model).filter_by(**kwargs)
        query = await self.session.execute(stmt)
        try:
            result = query.scalars().one()
        except NoResultFound as ex:
            raise ObjectNotFound from ex
        return result
