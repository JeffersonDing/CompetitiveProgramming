nums= [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
def maxSubArraySum(a):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, len(a)):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far
print(maxSubArraySum(nums))

def maxSubArraySumNeg(a):

    max_so_far =a[0]
    curr_max = a[0]

    for i in range(1,len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)

    return max_so_far
print(maxSubArraySumNeg(nums))
