from libForArea import Area


def main():
    example = Area()
    # Площадь круга с радиусом 12
    print(example.circle(radius=12))
    # Площадь треугольника со сторонами 3, 4, 5
    print(example.triangle(a_side=3, b_side=6, c_side=7))


if __name__ == "__main__":
    main()
