n = int(input())
breed = input().split(" ")
count = 0
isEven = True
even = []
odd = []

for x in breed:
    if(int(x) % 2 == 0):
        even.append(int(x))
    else:
        odd.append(int(x))

for i in range(min(len(even), len(odd))):
    count += 2
    even.pop(0)
    odd.pop(0)

if(even != []):
    even.pop(0)
    count += 1
    isEven = not isEven

if(len(odd) < 7):
    if(isEven):
        count += (len(odd)+1)/2
    else:
        count +=
else:
    for i in range(len(odd)):
        if(len(odd) == 7):
            if(isEven):
                count += 3
                break
            else:
                count += 5
                break
        else:
            count += 1
            if(isEven):
                odd.pop(0)
                odd.pop(0)
            else:
                odd.pop(0)
            isEven = not isEven

print(int(count))
