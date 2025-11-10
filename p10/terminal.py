from order import Order
from pizza import PizzaPepperoni, PizzaBarbecue, PizzaSea


class Terminal:
    """Класс Терминал обеспечивает взаимодействие с клиентом."""

    COMPANY = "Freddy Pizza"
    COMAND_CANCEL_ORDER = -1
    COMAND_CONFIRMATION_ORDER = 0

    def __init__(self):
        """Конструктор класса.
        self.меню: список доступных пицц;
        self.заказ: список заказанных пицц;
        self.отображать_меню: определяет отображение меню
        равен True: при создании терминала,
        после отмены или подтверждения заказа.
        """
        # Доступные пиццы
        self.menu = [PizzaPepperoni(), PizzaBarbecue(), PizzaSea()]
        self.order = None
        self.display_menu = True

    def __str__(self):
        """Вернуть строковое представление класса.

        Формат вывода:

        Имя пиццерии, версия программы.
        """
        return f"{Terminal.COMPANY} #1"

    def show_menu(self):
        """Показать меню.

        Показать меню следует только при наличии флага self.отображать_меню
        self.отображать_меню устанавливается в False после вывода меню.

        Формат вывода:

        Пиццерия #1
        Добро пожаловать!

        Меню:
        1. Пицца: Пепперони | Цена: 350.00 р.
        Тесто: тонкое Соус: томатный
        Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
        Тесто: тонкое Соус: барбекю
        Начинка: бекон, ветчина, зелень, сыр моцарелла
        3. Пицца: Дары моря | Цена: 550.00 р.
        Тесто: пышное Соус: тар-тар
        Начинка: кальмары, креветки, мидии, сыр моцарелла
        Для выбора укажите цифру через <ENTER>.
        Для отмены заказа введите -1
        Для подтверждения заказа введите 0
        """
        if not self.display_menu:
            return
        pepperoni = PizzaPepperoni()
        barbecue = PizzaBarbecue()
        sea = PizzaSea()

        res = f"""Пиццерия #1
        Добро пожаловать!

        Меню:
        1. {pepperoni}
        2. {barbecue}
        3. {sea}

        Для выбора укажите цифру через <ENTER>.
        Для отмены заказа введите -1
        Для подтверждения заказа введите 0"""

        print(res)
        self.display_menu = False

    def process_comand(self, point_menu):
        """Обработать действие пользователя.

        Аргументы:
        - пункт_меню (str): выбор пользователя.

        Возможные значения "пункт_меню":
        - -1: отменить заказ;
        - 0: подтвердить заказ; при этом осуществляется
        выставление счета, оплата, а также выполняется заказ;
        после заказ удаляется (= None)
        - 1..len(self.меню): добавление пиццы к добавить_к_заказу;
        если заказ не создан, его нужно создать.
        - иначе: сообщить о невозможности обработать команду.

        Каждое действие подтверждается выводом на экран, например:
        1
        Пицца Пепперони добавлена!
        2
        Пицца Барбекю добавлена!
        0
        Заказ подтвержен.
        """
        try:
            point_menu = int(point_menu)
            if point_menu == Terminal.COMAND_CANCEL_ORDER:
                self.order = None
                self.display_menu = True
                print("Ваш заказ отменён")
            elif point_menu == Terminal.COMAND_CONFIRMATION_ORDER:
                if self.order and self.order.ordered_pizzas:
                    print(f"Ваш заказ подтверждён")
                    print(self.order)
                    self.process_payment()

                    print("\n" + self.order.make())
                    self.order = None
                    self.display_menu = True
                else:
                    print("Заказ пуст!")
                # Уберите raise и добавьте необходимый код
                # Проверьте, что подтверждение вызывается для созданного заказа
                # При возникновении ошибки необходимо вызвать команду
                # отмены заказа
            elif 1 <= point_menu <= len(self.menu):
                if self.order is None:
                    self.order = Order()
                self.order.add(self.menu[point_menu - 1])
                # Уберите raise и добавьте необходимый код
                # Если заказ не создан, его нужно предварительно создать
                print(f"Пицца {self.menu[point_menu - 1].title} добавлена!")
            else:
                # За границей меню передаем управление в обработку исключений
                raise ValueError
        except ValueError:
            print("Не могу распознать команду! Проверьте ввод.")
        except Exception:
            print("Во время работы терминала произошла ошибка...")
            self.order = None
            self.display_menu = True

    def process_payment(self):
        try:
            total = self.order.summ()
            print(f"Сумма к оплате: {total:.2f} р.")
            pay = float(input("Введите сумму: "))

            if pay < total:
                print("Недостаточно средств! Заказ отменен.")
                self.order = None
                self.display_menu = True
                return False

            change = pay - total
            print(f"Вы внесли {pay:.2f} р. Сдача: {change:.2f} р.")
            return True

        except ValueError:
            print("Ошибка ввода суммы! Заказ отменен.")
            self.order = None
            self.display_menu = True
            return False