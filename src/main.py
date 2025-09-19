from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from src.api.customers import router as customer_router
from src.api.orders import router as order_router
from src.api.analytics import router as analytics
from src.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(customer_router)
app.include_router(order_router)
app.include_router(analytics)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
