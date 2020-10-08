def run(index):
    global total
    if(price[index]==0):
        return
    if(price[index-1]==0 or index-1<0):
        total+=price[index]
        price[index]=0
        return
    elif(price[index-2]==0 or index-2<0):
        total+=price[index-1]+price[index]*0.75
        price[index-1]=0
        price[index]=0
        return
    else:
        total+=price[index-2]+price[index-1]+price[index]*0.5
        price[index]=0
        price[index-1]=0
        price[index-2]=0
        return

total=0
N=int(input())
price=[]
for x in range(0,N):
    price.append(int(input()))
while(max(price)!=0):
    print(price)
    m=max(price)
    indexs = [i for i, j in enumerate(price) if j == m]
    print(indexs)
    run(indexs[-1])
print(total)
