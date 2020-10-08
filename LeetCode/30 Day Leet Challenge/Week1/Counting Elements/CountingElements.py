#Solution 1 64ms
#from collections import defaultdict
#arr= [1,1,3,3,5,5,7,7]
#count=0
#amount=defaultdict(list)
#for x in arr:
#    amount[x].append(x)
#for x in arr:
#    if x+1 in list(amount.keys()):
#        count+=1
#print(count)

#Solution 2 44ms
#arr= [1,1,3,3,5,5,7,7]
#count = 0
#ans=list(set(arr))
#for x in arr:
#    if x+1 in ans:
#        count+=1
#print(count)


#Solution 3 20ms
#from collections import defaultdict
#arr= [1,3,2,3,5,0]
#count=0
#amount=defaultdict(bool)
#for x in arr:
#    amount[x]=True
#for x in arr:
#    if(amount[x+1]==True):
#        count+=1
#print(count)
#Solution 4 24ms
from collections import defaultdict
arr= [1,3,2,3,5,0]
arr=sorted(arr,reverse=True)
count=0
amount=defaultdict(bool)
for x in arr:
    amount[x]=True
    if(amount[x+1]==True):
        count+=1
print(count)
