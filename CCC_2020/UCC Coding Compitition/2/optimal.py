N = int(input())
lifts=[]
curr=-1
for x in range(0,N):
    M=input()
    amt = int(M.split()[0])
    lifts.append([])
    for y in M.split():
        lifts[-1].append(int(y))
for x in lifts:
    this=0
    for y in range(1,len(x)):
        this+=x[y]
    if(this<curr or curr==-1):
        curr=this
print(curr)
