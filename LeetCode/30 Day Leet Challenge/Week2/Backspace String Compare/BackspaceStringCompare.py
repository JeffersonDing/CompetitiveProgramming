S = "ab#c"
T = "ad#c"
def build(str):
    arr=[]
    for x in str:
        if(x!='#'):
            arr.append(x)
        elif(x=='#'):
            arr.pop()
    return("".join(arr))
print(build(S)==build(T))
