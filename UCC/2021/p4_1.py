def pisano(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr \
            = curr, (prev + curr) % m
        if (prev == 0 and curr == 1):
            return i + 1


def fibMod(n, m):
    pisano_period = pisano(m)
    n = n % pisano_period
    prev, curr = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        prev, curr \
            = curr, prev + curr
    return (curr % m)


def strength(p):
    return fibMod(p, 2021)+(p % 50)


time = 0

N = int(input())
location = 1

while(location != N):
    if(location + strength(location) > N):
        diff = N-location
        best = (0, 0)
        for i in range(location):
            attempt = (location-i)+(strength(location-i))
            if(attempt <= N and attempt > best[1]):
                best = (i, attempt)
                break
        if(best[0] < diff):
            location = best[1]
            time += best[0]+1
            continue
        location += diff
        time += diff
        continue
    else:
        location += strength(location)
        time += 1
print(time)
