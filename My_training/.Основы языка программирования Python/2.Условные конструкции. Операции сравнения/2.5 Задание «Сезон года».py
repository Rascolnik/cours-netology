def check_month(month: int):
    """Напишите ваш код здесь"""
    if month == 1 or month == 2 or month == 12:
        season = "Зима"
    elif month == 3 or month == 4 or month == 5:
        season = "Весна"
    elif month == 6 or month == 7 or month == 8:
        season = "Лето"
    elif month == 9 or month == 10 or month == 11:
        season = "Осень"
    else:
        season = "Некорректный номер месяца"
    return season






if __name__ == '__main__':
    # Этот код менять не надо
    season = check_month(1)
    assert season == 'Зима', "Ответ должен быть Зима"
    print(f"1 месяц время года: {season}")
    season = check_month(4)
    assert season == 'Весна', "Ответ должен быть Весна"
    print(f"4 месяц время года: {season}")
    season = check_month(18)
    assert season == "Некорректный номер месяца", "Ответ должен быть 'Некорректный номер месяца'"
    print(f"18 месяц: {season}")
