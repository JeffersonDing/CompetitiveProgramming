N = int(input())
rowx=input()
rowy=input()
row1=[]
row2=[]
for x in rowx:
    row1.append(x)
for y in rowy:
    row2.append(y)

for i in range(0,len(row1)):
    if(int(row1[i])==1 or int(row2[i])==1):
        N=N-1
print(N)
