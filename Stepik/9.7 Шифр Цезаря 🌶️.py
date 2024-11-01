num = int(input())
code_message = input()
message = ""
for char in code_message:
    char_num = ord(char) - num
    if ord('a') <= char_num <= ord('z'):
        message += chr(char_num)
    elif char_num < ord('a'):
        message += chr(ord('z') - (ord('a') - char_num + 1))

print(message)
