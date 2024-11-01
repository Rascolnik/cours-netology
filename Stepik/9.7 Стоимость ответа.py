def calculate_message_cost(message):
    """Calculates the cost of a message in bee tokens.

    Args:
        message: The message string.

    Returns:
        A string representing the message and its cost.
        ПЕРЕВОД:
        Вычисляет стоимость сообщения в пчелиных жетонах.

    Аргументы:
        message: строка с сообщением.

    Возвращает:
        строку, представляющую сообщение и его стоимость.
    """

    total_cost = 0
    for char in message:
        total_cost += ord(char) * 3

    return f"Текст сообщения: '{message}'\nСтоимость сообщения: {total_cost}🐝"


if __name__ == "__main__":
    message = input()
    result = calculate_message_cost(message)
    print(result)

            #решение для степика:
message = input()
total_cost = 0
for char in message:
    total_cost += ord(char) * 3

print(f"Текст сообщения: '{message}'\nСтоимость сообщения: {total_cost}🐝")