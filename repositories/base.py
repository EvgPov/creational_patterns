from abc import ABC, abstractmethod
from models.order import Order
from typing import List, Optional


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order):
        pass
    @abstractmethod
    def get_all(self) -> List[Order]:
        pass
    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[Order]:
        pass