strs=["eat", "tea", "tan", "ate", "nat", "bat"]
ans=[]
#index=[];
#for i in range(len(strs)):
#    index.append([strs[i],i])
#for i in range(len(index)):
#    for j in index[i][0]:
#        index[i][0]=sorted(index[i][0])
#index.sort()
#print(index)
from collections import defaultdict
def printAnagramsTogether(words):
    groupedWords = defaultdict(list)
    for word in words:
        groupedWords["".join(sorted(word))].append(word)
    for group in groupedWords.values():
        ans.append(group)
printAnagramsTogether(strs);
print(ans)
