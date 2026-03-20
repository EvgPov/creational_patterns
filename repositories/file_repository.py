import json
from models.order import Order
from repositories.base import OrderRepository
from typing import List
import os
from pathlib import Path

class FileOrderRepository(OrderRepository):
    def __init__(self, filename: str = "data/orders.json"):
        self.filename = filename
        self.orders: List[Order] = self._load()
        if not self.orders and not os.path.exists(filename):
            self._save()

    def _load(self) -> List[Order]:
        if not Path(self.filename).is_file():
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError, TypeError, KeyError):
            print(f"{self.filename} повреждён или отсутствует")
            return []

        if not isinstance(data, list):
            print(f"{self.filename} не содержит список")
            return []

        orders = []
        for i, item in enumerate(data, 1):
            if not isinstance(item, dict):
                print(f"Элемент {i} не словарь → пропущен: {item}")
                continue
            try:
                orders.append(Order.from_dict(item))
            except Exception as e:
                print(f"Ошибка в заказе #{i}: {e}\nДанные: {item}")
        return orders

    def _save(self):
        data = [order.to_dict() for order in self.orders]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def add(self, order: Order):
        self.orders.append(order)
        self._save()

    def get_all(self):
        return self.orders[:]

    def get_by_id(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None