n = input()
x = 0
s = 0
for i in n:
    if n.find('f',x)> 0:
        s = n.find('f',x)
        print(s)
        x = s + 1
if s < 0:
    print('NO')

