a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i**0.5) + 1):  # Проверка делителей до квадратного корня из i
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)