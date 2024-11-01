a, b, c, d = input(), input(), input(), input()
sum_a, sum_b, sum_c, sum_d, = 0, 0, 0, 0

for i in a:
    sum_a += ord(i)
for j in b:
    sum_b += ord(j)
for k in c:
    sum_c += ord(k)
for l in d:
    sum_d += ord(l)

result = max(sum_a, sum_b, sum_c, sum_d)

if sum_a == result:
    print(a)
elif sum_b == result:
    print(b)
elif sum_c == result:
    print(c)
elif sum_d == result:
    print(d)
