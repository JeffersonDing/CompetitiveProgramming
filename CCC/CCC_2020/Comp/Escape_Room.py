M=int(input())
N=int(input())
factors=[]
flag=False
aM=[]
def findExit(x,y):
    posible=[]
    for i in range(0,len(aM)):
        for p in range(0,len(aM[i])):
            if(int(aM[i][p])==x*y and i*p!=x*y):
                if(int(aM[0][0])==x*y):
                    print('yes')
                    exit()
                else:
                    posible.append([i,p])

    if(posible==[]):
        flag=False
        return
    splitCases(posible)

def splitCases(x):
    for i in x:
        findExit(i[0],i[1])

for x in range(0,M):
    aM.append(input().split(' '))
findExit(M,N)
if(flag==False):
    print('no')
