from math import pi

# Было бы интересно решить данную задачу через наследование, несколько классов,
# к примеру class Area, class Square и так далее, но это затруднит добавление новых фигур


class Area:

    "Класс для вычисление площади фигур"

    def __init__(self) -> None:
        pass

    def _triangle_check(self, a_side: float, b_side: float, c_side: float) -> None:
        "Функция проверки верности введенных данных"

        if type(a_side) not in [int, float] \
                or type(b_side) not in [int, float] \
                or type(c_side) not in [int, float]:
            raise TypeError("Неверный тип данных")

        if a_side < 0 or a_side < 0 or a_side < 0:
            raise ValueError("Сторона меньше нуля")

    def _circle_check(self, radius: float) -> None:
        "Функция проверки верности введенных данных"

        if type(radius) not in [int, float]:
            raise TypeError("Неверный тип данных")

        if radius < 0:
            raise ValueError("Радиус меньше нуля")

    def _sqrt(self, number: float) -> float:
        "Функция вычисление корня"

        if number < 0:
            raise ValueError("Нельзя взять корень из отрицательного числа")

        root = number ** 0.5
        return root

    def _pow(self, number: float, exp: int) -> float:
        "Функция возведения в степень"

        powed_num = number ** exp
        return powed_num

    def circle(self, radius: float) -> float:
        "Функция вычисления площади круга через радиус"

        self._circle_check(radius)

        area = pi * self._pow(radius, 2)
        return area

    def triangle(self, a_side: float, b_side: float, c_side: float) -> float:
        "Функция вычисления площади треугольника через формулу Герона"

        self._triangle_check(a_side, b_side, c_side)

        half_meter = (a_side + b_side + c_side) / 2
        product = half_meter * (half_meter - a_side) * \
            (half_meter - b_side) * (half_meter - c_side)

        if product < 0:
            raise ValueError("Треугольник с такими сторонами не существует")

        area = self._sqrt(product)
        return area

    def is_right_angled_triangle(self, a_side: float, b_side: float, c_side: float) -> bool:
        "Функция для проверки треугольника на прямоугольность"

        self._triangle_check(a_side, b_side, c_side)

        sides = sorted([a_side, b_side, c_side])
        squares = [side**2 for side in sides]
        return squares[2] == squares[0] + squares[1]
