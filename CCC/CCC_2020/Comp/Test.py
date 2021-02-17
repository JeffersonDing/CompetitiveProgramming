def rotate(l, n):
    return l[n:] + l[:n]
S=['A','B','C','H']
print(rotate(S,3))
