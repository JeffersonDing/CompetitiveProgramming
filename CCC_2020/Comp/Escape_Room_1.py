import pdb
#pdb.set_trace()
M=3
N=4
factors=[]
flag=False;
aM=[[3,10,8,14],[1,11,12,12],[6,2,3,90]]
def factor(x):
    factors=[]
    for i in range(1, x + 1):
       if x % i == 0:
           if(x/i>M or x/i>N or i>M or i>N):
               break
           else:
               factors.append([int(x/i),i])
def findExit(x,y):
    posible=[]
    for i in range(0,len(aM)):
        for p in range(0,len(aM[i])):
            if(int(aM[i][p])==x*y and i*p!=x*y):
                if(aM[0][0]==x*y):
                    print('yes')
                    break
                else:
                    posible.append([i,p])

    if(posible==[]):
        print('empty no')
        return
    splitCases(posible)
def splitCases(x):
    for i in x:
        findExit(i[0],i[1])
        print("ran",x)


findExit(M,N)
