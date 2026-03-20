from repositories.base import OrderRepository
from typing import List
from models.order import Order

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders: List[Order] = []

    def add(self, order: Order):
        self.orders.append(order)

    def get_all(self):
        return self.orders[:]

    def get_by_id(self, order_id: str):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None
