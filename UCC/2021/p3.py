N = int(input())
[x, y] = [int(i) for i in input().split(" ")]
R = int(input())
pizza = [0]*N
count = 0
for i in range(R):
    [a, b] = [int(i) for i in input().split(" ")]
    if(b < x or a > y):
        continue
    count += min(y, b)-max(x, a)+1
print(count)
