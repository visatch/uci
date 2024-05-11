from typing import List
import math

def shell_sort2(nums: List[int]):
    n = len(nums)
    gap_seq = []

    k = math.ceil(math.log2(n)) 

    for i in range(k,0,-1):
        print("i: " + str(i))
        gap_seq.append(2**i+1)
    
    #A083318 a(0) = 1; for n>0, a(n) = 2^n + 1.
    gap_seq.append(1)

    for gap in gap_seq:
        for i in range(gap,n):
            tmp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > tmp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = tmp

    return nums
