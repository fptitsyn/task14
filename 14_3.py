def f1(x, q):
    a = []
    while x > 0:
        a.append(x % q)
        x //= q
    return a[::-1]


for x in range(1, 5000):
    d = 5**2026 + 7*5**1013 + 107 - x
    k = f1(d, 6)
    if k.count(5) - k.count(0) == 28:
        print(x)
        break

