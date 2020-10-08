nums=[4,2,2,1,1]
#duplicate=list(set(nums))
#ans=[]
#ans.extend(nums)
#for i in duplicate:
#    nums.remove(i)
#print(nums)
#print(ans)
#for i in nums:
#    ans.remove(i)
#    ans.remove(i)
#print(int(ans[0]))
def single_number(arr):
    result = 0
    for i in arr:
        result ^= i
    return result
print(single_number(nums))
