n = input()
t = ['А','В','Е','К','М','Н','О','Р','С','Т','У','Х']

if n[0] in t and n[4] in t and n[5] in t and len(n) == 9 :
    if n.isupper() and n[0].isalpha and n[1:4].isdigit() and n[1:4] != "000"  and n[4:6].isalpha() and n[7:-1].isdigit():
        print('YES')
    else:
        print('NO')
else:
    print('NO')


