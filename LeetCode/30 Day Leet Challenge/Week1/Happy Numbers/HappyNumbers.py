#def FindHappy(n):
#    list_n=[n,]
#    l=0
#    ls=0
#    num=0
#    while num != 1:
#        if l != ls:
#            return False
#        num = sum([int(i)**2 for i in list(str(n))])
#        list_n.append(num)
#        l= len(list_n)
#        ls=len(set(list_n))
#        n=num # reset n after each sum calculation
#        return True
#print(FindHappy(2))
def isHappy(self,n):
    list_n, l, ls, num = [n,], 0, 0, 0
    while num != 1:
        if l != ls:
            return False
        num = sum([int(i)**2 for i in list(str(n))])
        list_n.append(num)
        l, ls = len(list_n), len(set(list_n))
        n=num
    return True
