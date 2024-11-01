def list_of_numbers(n: int) -> list:
    result = [] #создаем пустой список
    for i in range(1,n+1):
        result.append(i) # добавляем элемент в список
    return result

if __name__ == '__main__':
    assert list_of_numbers(1) == [1]
    assert list_of_numbers(5) == [1, 2, 3, 4, 5]
    assert list_of_numbers(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nОтличная работа, отправляйте на проверку!")