from fastapi import APIRouter


from src.repositories.uow import SqlAlchemyUoW
from src.api.deps.dependencies import DBSession
from src.service.customers import CustomerService
from src.shemas.schemas import Customer

router = APIRouter(tags=["Customers"])


@router.get("/customers", response_model=list[Customer])
async def get_all_customers(db: DBSession):
    uow = SqlAlchemyUoW(db)
    return await CustomerService(uow).get_all()
