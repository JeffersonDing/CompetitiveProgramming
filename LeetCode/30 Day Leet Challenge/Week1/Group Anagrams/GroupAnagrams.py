words=["eat", "tea", "tan", "ate", "nat", "bat"]
index=[];
ans=[];
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]
#for i in words:
#    ans.append(sorted(list(i)))
#for i in words:
#    if(duplicates(ans,(sorted(list(i)))) not in index):
#        index.append(duplicates(ans,(sorted(list(i)))))
#for i in range(0,len(index)):
#    for j in range(0,len(index[i])):
#        index[i][j]=words[index[i][j]]
primes ={
'a': 2,
'b': 3,
'c': 5,
'd': 7,
'e': 11,
'f': 13,
'g': 17,
'h': 19,
'i': 23,
'j': 29,
'k': 31,
'l': 37,
'm': 41,
'n': 43,
'o': 47,
'p': 53,
'q': 59,
'r': 61,
's': 67,
't': 71,
'u': 73,
'v': 79,
'w': 83,
'x': 89,
'y': 97,
'z': 101
}
for i in words:
    sum=1
    for x in list(i):
        sum*=primes[x]
    ans.append(sum)
for i in ans:
    if(duplicates(ans,i) not in index):
        index.append(duplicates(ans,i))
for i in range(0,len(index)):
    for j in range(0,len(index[i])):
       index[i][j]=words[index[i][j]]
print(index)
