"""Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
Выдвигаем гипотезу: мы получим лучшие рекомендации, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки.

Обратите внимание, что если количество людей в списках будет не совпадать, то мы никого не будем знакомить и выведем пользователю предупреждение, что кто-то может остаться без пары.
"""
def solve(boys: list, girls: list):
    result = ""  # в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"

    if len(boys) == len(girls): # проверьте, что длины списков одинаковы
        pairs = []

        for boy, girl in zip(sorted(boys),sorted(girls)):  # отсортируйте пары, объедините при помощи zip и распакуйте в цикле
            pairs.append(f"{boy} и {girl}")
        result = ", ".join(pairs)
    else:
        result = "Кто-то может остаться без пары!"
    return result


if __name__ == '__main__':
    # Этот код менять не нужно
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")
