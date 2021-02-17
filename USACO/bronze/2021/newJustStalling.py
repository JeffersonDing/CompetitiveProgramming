from itertools import permutations
from collections import Counter
n = int(input())
a = input().split(" ")
b = input().split(" ")
for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])

count = 0
possible = [list(zip(single, b)) for single in permutations(a, len(b))]
for x in possible:
    for y in x:
        if(y[0] > y[1]):
            possible.remove(x)

for x in possible:
    x.sort(key=lambda tup: tup[0])
out = []
for x in possible:
    if x not in out:
        out.append(x)

print(len(out))
