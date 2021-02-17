tmp = input()
heard = input()
alpha = {}
count = 1
for i in range(0, len(tmp)):
    alpha[tmp[i]] = i

for j in range(0, len(heard)-1):
    if(alpha[heard[j]] >= alpha[heard[j+1]]):
        count += 1
print(count)
