from models.dish import Dish
from typing import Optional
from models.combo_meal import ComboMeal

class ComboMealBuilder:
    def __init__(self):
        self.main: Optional[Dish] = None
        self.drink: Optional[Dish] = None
        self.dessert: Optional[Dish] = None
        self.discount_percent: float = 10.0

    def add_main(self, dish: Dish) -> "ComboMealBuilder":
        self.main = dish
        return self

    def add_drink(self, dish: Dish) -> "ComboMealBuilder":
        self.drink = dish
        return self

    def add_dessert(self, dish: Dish) -> "ComboMealBuilder":
        self.dessert = dish
        return self

    def add_discount(self, discount_persent: float):
        self.discount_percent = discount_persent
        return self

    def build(self) -> ComboMeal:
        if not self.main:
            raise ValueError("Основное блюдо обязательно")
        return ComboMeal(
            main = self.main,
            drink = self.drink,
            dessert = self.dessert,
            discount_percent = self.discount_percent
        )


