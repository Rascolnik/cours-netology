def sum_cubes(num1: int, num2: int):
    return f"Для чисел {num1} и {num2}:\n" \
           f"  Сумма кубов: {num1}**3 + {num2}**3 = {num1 ** 3 + num2 ** 3}\n" \
           f"  Куб суммы: ({num1} + {num2})**3 = {(num1 + num2) ** 3}"


print(sum_cubes(1, 2))
