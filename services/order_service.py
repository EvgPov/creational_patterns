from repositories.base import OrderRepository
from models.order import Order
from typing import List

class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def add_order(self, order: Order)-> Order | None :
        self.repository.add(order)

    def get_all_orders(self) -> List[Order]:
        return self.repository.get_all()

    def get_order_by_id(self, order_id: str) -> Order:
        return self.repository.get_by_id(order_id)

    def change_status(self, order_id: str, new_status: str):
        order = self.get_order_by_id(order_id)
        if order:
            order.status = new_status
