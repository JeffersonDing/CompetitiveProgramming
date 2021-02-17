N = int(input())
k = int(input())
sum = 0
for i in range(k):
    sum += N
    N = int(str(N)+"0")
print(sum)
