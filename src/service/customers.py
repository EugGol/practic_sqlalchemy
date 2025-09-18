from src.service.base import BaseService


class CustomerService(BaseService):
    async def get_all(self):
        return await self.uow.customer.get_all()
