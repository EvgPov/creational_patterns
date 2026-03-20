from models.dish import Dish
from typing import List
import uuid
from datetime import datetime
from models.dish import Pizza, Sushi, Drink, Dessert, Salad, Burger

class Order:
    def __init__(self, table_number: int, items: List[Dish], status: str = 'Создан'):
        self.id = str(uuid.uuid4())
        self.date = datetime.now().strftime('%d-%m-%Y %H:%M')
        self.table_number = table_number
        self.items = items
        self.status = status

    def get_total(self) -> float:
        return sum(item.get_price() for item in self.items)

    def __str__(self):
        names = ", ".join(item.get_name() for item in self.items)
        return (f"Заказ #{self.id[:8]} | Стол {self.table_number} | "
                f"Статус: {self.status} | Сумма: {self.get_total():.0f} руб. | "
                f"Блюда: {names}")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "date": self.date,
            "table_number": self.table_number,
            "status": self.status,
             "items": [
                 {
                     "name": item.get_name(),
                     "price": item.get_price(),
                     "type": item.__class__.__name__
                 }
                 for item in self.items
             ]
        }

    @staticmethod
    def from_dict(data: dict) -> 'Order':
        DISH_CLASSES = {
            'Pizza': Pizza,
            'Sushi': Sushi,
            'Drink': Drink,
            'Dessert': Dessert,
            'Burger': Burger,
            'Salad': Salad,
        }
        order=Order(table_number=int(data.get('table_number', 0)), items=[], status=data.get('status', "Создан"))
        order.id = data['id']
        order.date =data.get("date", datetime.now().strftime("%d.%m.%Y %H:%M"))

        for item_data in data.get('items', []):
            cls_name = item_data.get('type', 'Drink')  # fallback
            dish_class = DISH_CLASSES.get(cls_name, Drink)

            dish = dish_class(name=item_data.get('name', '???'), price=float(item_data.get('price', 0)))
            order.items.append(dish)
        return order