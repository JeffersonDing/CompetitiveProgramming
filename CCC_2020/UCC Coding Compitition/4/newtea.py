import sys
sys.setrecursionlimit(10000000)
def cost(x):
    length = len(x);
    if(length==0):
        return 0;
    elif(length==1):
        return x[0];
    elif(length==2):
        return max(x[0], x[1])+min(x[0], x[1])*0.75;
    elif(length==3):
        discount = min(x[0], x[1],x[2]);
        x.remove(discount);
        return discount*0.5+x[0]+x[1];
def solve(n):
    l = len(n);
    if(l<3):
        return cost(n);
    else:
        if(tuple(n) not in seen):
            one,two,three=[],[],[]
            one.extend(n)
            one.pop(-1)
            two.extend(one)
            two.pop(-1)
            three.extend(two)
            three.pop(-1)
            a=cost([n[l-1]])+solve(one)
            b=cost([n[l-1],n[l-2]])+solve(two)
            c=cost([n[l-1],n[l-2],n[l-3]])+solve(three)
            optimal=min(a,b,c)
            seen[tuple(n)]=optimal;
    return seen[tuple(n)]
N = int(input())
prices=[]
seen={}
for x in range(0,N):
    prices.append(int(input()))
print(solve(prices))
