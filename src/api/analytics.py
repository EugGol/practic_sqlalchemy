from fastapi import APIRouter, HTTPException, Query
from src.api.deps.dependencies import DBSession
from src.exceptions import InvalidDateRangeError
from src.repositories.uow import SqlAlchemyUoW
from src.service.analytics import AnalyticsService
from src.shemas.analytics import TopProductsRequest


router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/top_products")
async def get_analytics(db: DBSession, request: TopProductsRequest = Query()):
    uow = SqlAlchemyUoW(db)
    try:
        result = await AnalyticsService(uow).get_top_products_by_period(request)
    except InvalidDateRangeError:
        raise HTTPException(status_code=400, detail="Invalid date range")
    return result
