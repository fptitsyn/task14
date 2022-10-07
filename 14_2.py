def f(x, q):
    s = 0
    for i in range(-1, -len(x) - 1, -1):
        s += x[i] * q ** (abs(i) - 1)

    return s


for x in range(15):
    for y in range(17):
        a1 = f([1, 2, 3, x, 5], 15)
        a2 = f([6, 7, y, 9], 17)
        if (a1 + a2) % 131 == 0:
            print(x, y, (a1 + a2) // 131)