def f1(x, q):
    a = []
    while x > 0:
        a.append(x % q)
        x //= q
    return a[::-1]


s = 16**44 * 16**30 - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))

a = f1(s, 16)
for i in range(len(a)):
    if a[i] == 14:
        a[i] = 1

a = [int(i) for i in a]
a.pop(-5)
print(a.count(1))
