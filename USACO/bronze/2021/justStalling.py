n = int(input())
a = input().split(" ")
b = input().split(" ")
for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])
count = 0
sorted(b)


def solve(curr, remain):
    global count
    if(remain == []):
        count += 1
        return
    if(curr >= n):
        return
    for i in remain:
        if(a[curr] <= i):
            stalls = remain.copy()
            stalls.remove(i)
            search = curr+1
            solve(search, stalls)


solve(0, b)
print(count)
