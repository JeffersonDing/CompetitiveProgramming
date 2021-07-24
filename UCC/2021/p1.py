# sample = "622544252"

coins = list(input())
count = 0
for i in range(len(coins)):
    if(coins[i] == "2"):
        try:
            if(coins[i+1] != "5"):
                count += 1
        except:
            count += 1
print(count)
