from src.exceptions import ObjectNotFound, ProductNotFound, UserNotFound
from src.service.base import BaseService


class OrderService(BaseService):
    async def get_order_with_product(self, id: int):
        orders_with_product = await self.uow.order.get_order_with_products_name(id=id)

        return orders_with_product

    async def create_order(self, request):
        await self.uow.product.count_by_ids(product_ids=request.products_ids)
        try:
            await self.uow.customer.get_one(id=request.user_id)
        except ObjectNotFound:
            raise UserNotFound
        new_order = await self.uow.order.create(
            user_id=request.user_id, created_at=request.created_at
        )
        order_id = new_order.id 
        product_ids = request.products_ids
        await self.uow.order_item.create_many(
            [
                {
                    "order_id": new_order.id,
                    "product_id": product_id,
                    "quantity": product_ids.count(product_id),
                }
                for product_id in product_ids
            ]
        )
        await self.uow.session.commit()

        return order_id
