from fastapi import APIRouter, HTTPException

from src.api.deps.dependencies import DBSession
from src.exceptions import ObjectNotFound, ProductNotFound, UserNotFound
from src.repositories.uow import SqlAlchemyUoW
from src.service.orders import OrderService
from src.shemas.schemas import OrderOutWithProducts, OrderRequestAdd

router = APIRouter(prefix="/orders", tags=["Orders"], )

@router.get("/{id}", response_model=OrderOutWithProducts)
async def get_order_with_product(id: int, db: DBSession):
    uow = SqlAlchemyUoW(db)
    try:
        orders_with_product = await OrderService(uow).get_order_with_product(id=id)
    except ObjectNotFound:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_with_product


@router.post("")
async def create_order(request: OrderRequestAdd, db: DBSession):
    uow = SqlAlchemyUoW(db)
    try:
        new_order_id = await OrderService(uow).create_order(request)
        
    except UserNotFound:
        raise HTTPException(status_code=404, detail="Create order failed. User not found")
    except ProductNotFound:
        raise HTTPException(status_code=404, detail="Create order failed. Product not found")
    return {"message": "Order created", "order_id": new_order_id}