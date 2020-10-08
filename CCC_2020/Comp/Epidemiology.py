P = int(input())#total 10 750
N = int(input())#day0 2 1
R = int(input())#infection rate 1 5
sum=N
count=0
while(sum<=P):
    N=N*R
    sum=sum+N
    count+=1

print(count)
