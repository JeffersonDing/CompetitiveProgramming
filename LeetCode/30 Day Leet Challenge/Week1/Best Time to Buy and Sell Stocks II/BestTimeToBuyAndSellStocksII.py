prices=[7,1,5,3,6,4]
max = 0;
for i in range(1,len(prices)):
    if(prices[i]>prices[i-1]):
        max+=prices[i]-prices[i-1]
print(max)
