nums=[1,0,0,0,1]
#def move(a):
#    if(all(x==0 for x in a)):
#        return
#    for i in range(0,len(a)):
#        if(a[i]==0):
#            a.insert(len(a),a[i])
#            a.pop(i)
#        if(a[0]==0):
#            move(a)
#move(nums)
#print(nums)

def pushZerosToEnd(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    while count < len(arr):
        arr[count] = 0
        count += 1
pushZerosToEnd(nums)
print(nums)
