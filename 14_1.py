def f(x, q):
    a = 0
    for i in range(-1, -len(x) - 1, -1):
        a += x[i] * q ** (abs(i) - 1)
    return a


for x in range(1, 8):
    for y in range(8):
        a1 = f([x, 0, 1, y, 4], 9)
        a2 = f([x, y, 5, 4, 4], 8)
        d = a1 + a2
        if d % 89 == 0:
            print(x, y)
            print(d // 89)
