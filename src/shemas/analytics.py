from datetime import date
from pydantic import BaseModel, Field


class TopProductsOut(BaseModel):
    product_id: int
    product_name: str
    price: float
    ordered_quantity: int


class TopProductsRequest(BaseModel):
    period_start: date = Field(
        ..., description="Укажите начальную дату периода выборки"
    )
    period_end: date = Field(..., description="Укажите конечную дату периода выборки")
