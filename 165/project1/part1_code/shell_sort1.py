from typing import List
import math

def shell_sort1(nums: List[int]):
    n = len(nums)
    gap_seq = []

    k = math.ceil(math.log2(n))

    for i in range(1,k):
        gap_seq.append(n // (2**i))
    
    for gap in gap_seq:
        for i in range(gap,n):
            tmp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > tmp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = tmp

    return nums


