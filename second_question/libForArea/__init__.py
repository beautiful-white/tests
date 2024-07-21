from math import pi

# Было бы интересно решить данную задачу через наследование, несколько классов,
# к примеру class Area, class Square и так далее, но это затруднит добавление новых фигур


class Area:

    "Класс для вычисление площади фигур"

    def __init__(self) -> None:
        pass

    def _sqrt(self, number: float) -> float:
        "Функция вычисление корня"

        assert number > 0, "Нельзя взять корень из отрицательного числа"

        root = number ** 0.5
        return root

    def _pow(self, number: float, exp: int) -> float:
        "Функция возведения в степень"

        powed_num = number ** exp
        return powed_num

    def circle(self, radius: float) -> float:
        "Функция вычисления площади круга через радиус"

        area = pi * self._pow(radius, 2)
        return area

    def triangle(self, a_side: float, b_side: float, c_side: float) -> float:
        "Функция вычисления площади треугольника через формулу Герона"

        half_meter = (a_side + b_side + c_side) / 2
        product = half_meter * (half_meter - a_side) * \
            (half_meter - b_side) * (half_meter - c_side)

        assert product > 0, "Треугольник с заданными сторонами не существует"

        area = self._sqrt(product)
        return area
