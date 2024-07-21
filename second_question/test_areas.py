from libForArea import Area


def test_circle_1():
    obj = Area()
    assert int(obj.circle(123)) == 47529, "Несовпадение ответа"


def test_circle_2():
    obj = Area()
    assert int(obj.circle(15)) == 706, "Несовпадение ответа"


def test_triangle_1():
    obj = Area()
    assert int(obj.triangle(3, 4, 5)) == 6, "Несовпадение ответа"


def test_triangle_2():
    obj = Area()
    assert int(obj.triangle(5, 6, 10)) == 11, "Несовпадение ответа"
