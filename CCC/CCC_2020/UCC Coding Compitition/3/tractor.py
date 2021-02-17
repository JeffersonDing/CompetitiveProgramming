import re
def split(word):
    return [char for char in word]

H=int(input())
T=int(input())
Tsx=input().split()
for x in Tsx:
    x=int(x)
M=int(input())
S=split(input())
for x in range(0,len(S)):
    if(S[x]!='1'):
        S[x]='X'
S=''.join(S)
gaps = len(max(re.compile("(X+X)*").findall(S)))
cho=0
for x in Tsx:
    if(int(x)<=gaps):
        cho=int(x)
if(H%cho == 0):
    print((H//cho))
else:
    print((H//cho)+1)
