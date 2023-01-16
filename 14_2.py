def intt(s, t):
    s = s[::-1]
    a = 0
    for i in range(len(s)):
        a += int(s[i]) * int(t) ** i
    return a


for x in range(10):
    a1 = intt("13", f"132{x}4")
    a2 = int(f"134{x}2", 13)
    d = abs(a1 - a2)
    if d % 30 == 0:
        print(x, d // 30)