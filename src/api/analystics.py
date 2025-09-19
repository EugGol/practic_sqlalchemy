from fastapi import APIRouter, HTTPException, Query
from src.api.deps.dependencies import DBSession
from src.exceptions import InvalidDateRangeError
from src.repositories.uow import SqlAlchemyUoW
from src.service.analystics import AnalysticsService
from src.shemas.analystics import TopProductsRequest


router = APIRouter(prefix="/analystics", tags=["Analystics"])


@router.get("/top_products")
async def get_analystics(db: DBSession, request: TopProductsRequest = Query()):
    uow = SqlAlchemyUoW(db)
    try:
        result = await AnalysticsService(uow).get_top_products_by_period(request)
    except InvalidDateRangeError:
        raise HTTPException(status_code=400, detail="Invalid date range")
    return result
