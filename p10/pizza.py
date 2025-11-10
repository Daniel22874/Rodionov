class Pizza:
    """Класс Пицца содержит общие атрибуты для пиццы."""

    def __init__(self):
        self.title = "Заготовка"
        self.dough = "тонкое"
        self.sauce = "кетчуп"
        self.filling = []
        self.price = 0

    def __str__(self):
        return f"Пицца: {self.title} | Цена: {self.price:.2f} р.\n" \
               f"Тесто: {self.dough} Соус: {self.sauce}\n" \
               f"Начинка: {', '.join(self.filling)}\n"

    def prepare(self):
        return f"Начинаю готовить пиццу {self.title}\n" \
               f"- замешиваю {self.dough} тесто...\n" \
               f"- добавляю соус: {self.sauce}...\n" \
               f"- и, конечно: {', '.join(self.filling)}...\n"

    def bake(self):
        return "Выпекаю пиццу... Готово!"

    def cut(self):
        return "Нарезаю на аппетитные кусочки..."

    def pack(self):
        return "Упаковываю в фирменную упаковку и готово!"


class PizzaPepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.title = "Пепперони"
        self.dough = "тонкое"
        self.sauce = "томатный"
        self.filling = ['пепперони', 'сыр моцарелла']
        self.price = 350.00


class PizzaBarbecue(Pizza):
    def __init__(self):
        super().__init__()
        self.title = "Барбекю"
        self.dough = "тонкое"
        self.sauce = "барбекю"
        self.filling = ['бекон', 'ветчина', 'зелень', 'сыр моцарелла']
        self.price = 450.00


class PizzaSea(Pizza):
    def __init__(self):
        super().__init__()
        self.title = "Дары моря"
        self.dough = "пышное"
        self.sauce = "тар-тар"
        self.filling = ['креветки', 'кальмары', 'сыр моцарелла', 'мидии']
        self.price = 550.00