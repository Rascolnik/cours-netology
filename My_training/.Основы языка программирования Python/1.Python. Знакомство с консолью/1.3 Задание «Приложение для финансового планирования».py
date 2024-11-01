# Задайте первоначальные значения

salary = 100000  # Заработная плата
percent_mortgage = 30  # Ипотека
percent_life = 50  # На жизнь

# Напишите свой код здесь
mortgage = (salary / 100 * 30) * 12
result = (salary / 100 * 50 - (mortgage / 12)) * 12

print('Ипотека:', mortgage)
print('Накопления:', result)