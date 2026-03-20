from typing import Optional
from models.dish import Dish

class ComboMeal(Dish):
    def __init__(
            self,
            main: Dish,
            drink: Optional[Dish],
            dessert: Optional[Dish] = None,
            discount_percent: float = 10.0
        ):
        self.main = main
        self.drink = drink
        self.dessert = dessert
        self.discount_percent = discount_percent

    def get_name(self) -> str:
        drink_name = self.drink.get_name() if self.drink else 'без напитка'
        dessert_name = self.dessert.get_name() if self.dessert else 'без десерта'
        return f"Комбо: {self.main.get_name()} - {drink_name} - {dessert_name}"

    def get_price(self) -> float:
        total = self.main.get_price()
        if self.drink:
            total = total + self.drink.get_price()
        if self.dessert:
            total = total + self.dessert.get_price()
        discount = 1 - (self.discount_percent / 100)
        return round(total * discount, 2)
