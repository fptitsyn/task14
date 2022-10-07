def f(x, q):
    s = 0
    for i in range(-1, -len(x) - 1, -1):
        s += x[i] * q ** (abs(i) - 1)

    return s


# ord
# chr

n = 10
for i in range(ord("A"), ord("Z")+1):
    print(n, chr(i))
    n += 1

ans = []
for a in range(55):
    a1 = [35, a, 34, 33]
    a2 = [2, 33, a, 34]
    if (f(a1, 55) - f(a2, 55)) % 29 == 0:
        ans.append(a)


a1 = [35, max(ans), 34, 33]
a2 = [2, 33, max(ans), 34]
a3 = [35, min(ans), 34, 33]
a4 = [2, 33, min(ans), 34]

b1 = f(a1, 55) - f(a2, 55)
b2 = f(a3, 55) - f(a4, 55)

print(abs(b1 - b2))