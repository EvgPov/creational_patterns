from abc import ABC, abstractmethod

class Dish(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
    @abstractmethod
    def get_price(self) -> float:
        pass

class Pizza(Dish):
    def __init__(self, name: str = 'Маргарита', price: float = 500.0):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price

class Burger(Dish):
    def __init__(self, name: str = 'Гамбургер', price: float = 350.0):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price

class Sushi(Dish):
    def __init__(self, name: str = 'Филадельфия', price: float = 320.0):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price

class Salad(Dish):
    def __init__(self, name: str = 'Цезарь', price: float = 220.0):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price

class Dessert(Dish):
    def __init__(self, name: str = 'Тирамису', price: float = 150.0):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price

class Drink(Dish):
    def __init__(self, name: str = 'Морс', price: float = 120.0):
        self.name = name
        self.price = price
    def get_name(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price

