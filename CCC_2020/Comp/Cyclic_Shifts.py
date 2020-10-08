T=input()
S=input()
def rotate(l, n):
    return l[n:] + l[:n]
cycle=[]
Ssplit=[]
temp=[]
tempString=''
for x in S:
    Ssplit.append(x)
temp=Ssplit

for y in range(0,len(Ssplit)):
    temp=rotate(temp,1)
    tempString=''.join(temp)
    cycle.append(tempString)
    temp=[]
    for q in tempString:
        temp.append(q)
for str in cycle:
    if(T.find(str)!=-1):
        print("yes")
        exit()
print("no")
