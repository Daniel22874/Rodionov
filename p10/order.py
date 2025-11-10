import time


class Order:
    count_orders = 0

    def __init__(self):
        self.ordered_pizzas = []
        Order.count_orders += 1
        self.order_number = Order.count_orders

    def __str__(self):
        res = f"Заказ №{self.order_number}\n"
        for i, pizza in enumerate(self.ordered_pizzas, 1):
            res += f"{i}. {pizza}"
        res += f"Сумма заказа: {self.summ():.2f} р.\n"
        return res

    def add(self, pizza):
        self.ordered_pizzas.append(pizza)

    def summ(self):
        total = 0
        for pizza in self.ordered_pizzas:
            total += pizza.price
        return total

    def make(self):
        result = "Заказ поступил на выполнение...\n"
        for i, pizza in enumerate(self.ordered_pizzas, 1):
            result += f"{i}. {pizza.title}\n"
            result += pizza.prepare()
            time.sleep(1)
            result += pizza.bake() + "\n"
            time.sleep(1)
            result += pizza.cut() + "\n"
            time.sleep(1)
            result += pizza.pack() + "\n"
            time.sleep(1)
            result += "\n"
        result += f"Заказ №{self.order_number} готов! Приятного аппетита!"
        return result