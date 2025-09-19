from datetime import datetime, time
from src.exceptions import InvalidDateRangeError
from src.service.base import BaseService


class AnalyticsService(BaseService):
    def check_date_valid(self, req):
        if req.period_start > req.period_end:
            raise InvalidDateRangeError
        return True

    async def get_top_products_by_period(self, request):
        self.check_date_valid(request)

        start_dt = datetime.combine(request.period_start, time.min)
        end_dt = datetime.combine(request.period_end, time.max)

        return await self.uow.analytics.get_top_products_by_period(
            start_dt=start_dt, end_dt=end_dt
        )
