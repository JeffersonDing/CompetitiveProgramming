nums = [3,3]
target = 6
arr={}
for x in range(0,len(nums)):
    c=target-nums[x]
    if(arr.get(c)!=None):
        print([arr.get(c),x])
    arr[nums[x]]=x
