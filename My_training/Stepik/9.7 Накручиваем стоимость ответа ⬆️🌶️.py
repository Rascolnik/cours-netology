def calculate_cost(text):
    cost = 0
    for char in text:
        cost += ord(char) * 3
    return cost

def replace_chars(text):
    replacements = {
        'e': 'е', 'y': 'у', 'o': 'о', 'p': 'р', 'a': 'а', 'x': 'х', 'c': 'с',
        'E': 'Е', 'T': 'Т', 'O': 'О', 'P': 'Р', 'A': 'А', 'H': 'Н', 'X': 'Х',
        'C': 'С', 'B': 'В', 'M': 'М'
    }
    new_text = ""
    for char in text:
        new_text += replacements.get(char, char)
    return new_text

input_text = input()
old_cost = calculate_cost(input_text)
new_text = replace_chars(input_text)
new_cost = calculate_cost(new_text)

print(f"Старая стоимость: {old_cost}🐝")
print(f"Новая стоимость: {new_cost}🐝")

