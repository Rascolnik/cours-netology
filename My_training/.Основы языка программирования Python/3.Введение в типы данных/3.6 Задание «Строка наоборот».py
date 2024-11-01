def reverse(string: str) -> str:
    # Напишите ваш код здесь
    res_string = ''
    for i in range(len(string)-1,-1, -1):
        res_string += string[i]
    return res_string.lower()
print(reverse("'!dlroW olleH'"))

# string = string.lower()
# revers = string[::-1]
# return revers