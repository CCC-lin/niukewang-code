def check(c, b, a):
    s = str(c) + str(b) + str(a)
    if len(s) != 9:
        return False
    if '0' in s:
        return False
    return len(set(s)) == 9

a = []
for i in range(1, 100):
    for j in range(i, 10000):
        c = i * j
        if check(c, i, j):
            a.append((c, i, j))
            
a.sort(key=lambda x: (x[0], x[1]))
for x in a:
    print(f"{x[0]} = {x[1]} x {x[2]}")
    