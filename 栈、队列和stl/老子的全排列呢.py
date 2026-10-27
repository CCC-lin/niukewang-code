import itertools

s = itertools.permutations(list(range(1, 9)))
for i in s:
    print(" ".join(map(str, i)))