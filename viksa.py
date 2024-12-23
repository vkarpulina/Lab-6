class Stank:
    def __init__(self, productivity, price, part_price):
        self.productivity = productivity
        self.price = price
        self.part_price = part_price

    def calculate_parts_for_payback(self):
        if self.part_price == 0:
            raise ValueError("Цена детали не может быть нулевой.")
        return self.price / self.part_price

    def calculate_payback_time(self, fixed_part_price):
        if fixed_part_price == 0:
            raise ValueError("Цена детали не может быть нулевой.")
        return self.price / (self.productivity * fixed_part_price)


class FrezernyStank(Stank):
    def __init__(self, productivity, price, part_price, cutter_type):
        super().__init__(productivity, price, part_price)
        self.cutter_type = cutter_type

    def calculate_parts_for_payback(self):
        if self.cutter_type == "плоская":
            multiplier = 1.1
        else:
            multiplier = 1.0

        return super().calculate_parts_for_payback() * multiplier

    def calculate_payback_time(self, fixed_part_price):
        time = super().calculate_payback_time(fixed_part_price)
        if self.cutter_type == "плоская":
            time *= 1.1
        return time


class StankWithCNC(Stank):
    def __init__(self, productivity, price, part_price, cnc_type):
        super().__init__(productivity, price, part_price)
        self.cnc_type = cnc_type

    def calculate_parts_for_payback(self):
        if self.cnc_type == "старый":
            multiplier = 1.2
        else:
            multiplier = 1.0

        return super().calculate_parts_for_payback() * multiplier

    def calculate_payback_time(self, fixed_part_price):
        time = super().calculate_payback_time(fixed_part_price)
        if self.cnc_type == "старый":
            time *= 1.2
        return time


# Пример использования:

# Создаем фрезерный станок с плоской фрезой
frezerny_stank = FrezernyStank(
    productivity=50, price=100000, part_price=500, cutter_type="плоская"
)
print(
    f"Фрезерный станок: Количество деталей для окупаемости: "
    f"{frezerny_stank.calculate_parts_for_payback():.2f}"
)
print(
    f"Фрезерный станок: Время окупаемости при фиксированной цене детали 500: "
    f"{frezerny_stank.calculate_payback_time(500):.2f} часов"
)

# Создаем станок с ЧПУ нового типа
stank_cnc = StankWithCNC(
    productivity=100, price=200000, part_price=400, cnc_type="новый"
)
print(
    f"Станок с ЧПУ: Количество деталей для окупаемости: "
    f"{stank_cnc.calculate_parts_for_payback():.2f}"
)
print(
    f"Станок с ЧПУ: Время окупаемости при фиксированной цене детали 400: "
    f"{stank_cnc.calculate_payback_time(400):.2f} часов"
)

    f"Станок с ЧПУ: Время окупаемости при фиксированной цене детали 400: {stank_cnc.calculate_payback_time(400):.2f} часов")
