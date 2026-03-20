from models.dish import Pizza, Burger, Sushi, Salad, Dessert, Drink
class DishFactory:
    @staticmethod
    def create_dish(dish_type: str, **kwargs):
        types = {
            'pizza': Pizza,
            'burger': Burger,
            'sushi': Sushi,
            'salad': Salad,
            'dessert': Dessert,
            'drink': Drink,
        }

        class_name = types.get(dish_type.lower().strip())
        if not class_name:
            raise ValueError(f'Неизвестный тип блюда: {dish_type}')
        return class_name(**kwargs)