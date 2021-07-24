N = int(input())
weights = input().split(" ")
output = []
temp = []
for i in range(len(weights)):
    if(int(weights[i]) % 2 != 0):
        if(sum(temp) > sum(output)):
            output = temp.copy()
        temp = []
    else:
        temp.append(int(weights[i]))
if(sum(temp) > sum(output)):
    print(sum(temp))
else:
    print(sum(output))
