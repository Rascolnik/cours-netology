# import math
#
# def discriminant(a, b, c):
#     """
#     Функция для нахождения дискриминанта
#     """
#     return b ** 2 - 4 * a * c
#
# def solution(a, b, c):
#     """
#     Функция для нахождения корней уравнения
#     """
#     D = discriminant(a, b, c)
#
#     if D < 0:
#         print("корней нет")
#     elif D == 0:
#         x = -b / (2 * a)
#         print(x)
#     else:
#         x1 = (-b + math.sqrt(D)) / (2 * a)
#         x2 = (-b - math.sqrt(D)) / (2 * a)
#         print(f"{x1} {x2}")
#
# if __name__ == '__main__':
#     solution(1, 8, 15)
#     solution(1, -13, 12)
#     solution(-4, 28, -49)
#     solution(1, 1, 1)
#


#




# решение без импорта библиотек
def discriminant(a, b, c):
    """
    Функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    Функция для нахождения корней уравнения
    """
    D = discriminant(a, b, c)

    if D < 0:
        print("корней нет")
    elif D == 0:
        x = -b / (2 * a)
        print(x)
    else:
        x1 = (-b + (D ** 0.5)) / (2 * a)
        x2 = (-b - (D ** 0.5)) / (2 * a)
        # Сортируем корни для вывода в порядке возрастания если требуется
        # if x1 > x2:
        #     x1, x2 = x2, x1
        print(x1, x2)


if __name__ == '__main__':
    solution(1, 8, 15)  # Вывод: -5.0 -3.0
    solution(1, -13, 12)  # Вывод: 1.0 12.0
    solution(-4, 28, -49)  # Вывод: 3.5
    solution(1, 1, 1)  # Вывод: корней нет
