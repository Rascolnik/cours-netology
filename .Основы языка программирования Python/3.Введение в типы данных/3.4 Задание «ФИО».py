from typing import List

def fio(initials: List[str]) -> str:
    if len(initials) != 3:
        raise ValueError("Список должен содержать 3 элемента: имя, фамилию и отчество.")
    return f"{initials[0]} {initials[1]} {initials[2]}" # initials[0][0]=> [0]взять 1 подстроку из списка [0]взять 1 символ из построки

# Пример использования
print(fio(["Иван", "Иванов", "Иванович"]))  # Вывод: Иван Иванов Иванович


