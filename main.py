from os import name

from factories.dish_factory import DishFactory
from models.order import Order
from repositories.file_repository import FileOrderRepository
from repositories.in_memory_repository import InMemoryOrderRepository
from services.order_service import OrderService
from builders.combo_builder import ComboMealBuilder

def main():
    print("========== Система управления заказами в кафе ==========\n")
    print("1 — In-Memory репозиторий")
    print("2 — Файловый репозиторий (JSON)")

    choice = input("Выберите тип репозитория: ").strip()

    if choice == "1":
        repository = InMemoryOrderRepository()
        add_demo = True
    else:
        repository = FileOrderRepository()
        add_demo = len(repository.get_all()) == 0

    service = OrderService(repository)
    factory = DishFactory()

    if  add_demo:
        print("Репозиторий пуст — добавляем демонстрационные заказы")


        # создаем отдельные блюда через фабрику
        pizza = factory.create_dish('pizza', name = "Пицца 'Маргарита'", price = 600)
        sushi = factory.create_dish('sushi', name="Суши 'Калифорния'", price=415)
        mors = factory.create_dish('drink', name="Морс 0.3", price=95)
        cola = factory.create_dish('drink', name="Cola 0.5", price=95)
        tiramisu = factory.create_dish('dessert', name="Тирамису", price=200)

        # создаем комбо через Строитель
        combo = (ComboMealBuilder()
                 .add_main(pizza)
                 .add_drink(cola)
                 .add_dessert(tiramisu)
                 .build())

        # создаем заказы
        order_first = Order(table_number=3, items=[sushi, mors])
        order_second = Order(table_number=10, items=[combo])

        service.add_order(order_first)
        service.add_order(order_second)

        # меняем статус
        service.change_status(order_first.id, "Готов")
    else:
        print("В репозитории уже есть заказы — загружаем существующие данные\n")
    # выводим результат
    orders = service.get_all_orders()
    if not orders:
        print("Заказов пока нет.")
    else:
        print("Заказы:")
        for order in orders:
            print(order)
    # поиск по ID
    if orders:
        example_order = orders[0]
        print(f"\nПример: заказ по ID {example_order.id[:8]}...")
        found = service.get_order_by_id(example_order.id)
        if found:
            print(found)
        else:
            print("Заказ не найден (возможно ошибка в методе get_order_by_id)")
    else:
        print("\nНет заказов для показа примера поиска")

if __name__ == '__main__':
    main()
