def string_slices(string: str) -> str:
    return string[2:-2]


if __name__ == '__main__':
    assert string_slices("%%Приказ об увольнении&#") == 'Приказ об увольнении'
    assert string_slices("%%Лучший студент на курсе!&#") == 'Лучший студент на курсе!'
    assert string_slices("%%Hello World!&#") == 'Hello World!'
    print("\nОтличная работа, отправляйте на проверку!")
