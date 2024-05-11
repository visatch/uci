from typing import List

#I tried to balance between using pre_defined gap_sequence and use a function to best the appropriate gap_sequence for the input arr
#However, it seems that it resulted in O(n) which still does not better than generate the gap_sequence much
#So, I chose to generate a gap_sequence everytime I run this function

# gap_sequence_reversed = [70368756760577, 17592192335873, 4398049656833, 1099513200641, 274878693377, 68719869953, 17180065793, 4295065601, 1073790977, 268460033, 67121153, 16783361, 4197377, 1050113, 262913, 65921, 16577, 4193, 1073, 281, 77, 23, 8, 1]

# def find_the_largest_given_array_but_smaller_than_length(arr,target):
#     return max((arr[i] for i in range(len(arr)-1,0,-1) if arr[i] < target), default=None)


def shell_sort4(nums: List[int]):
    n = len(nums)
    gap_seq = [1] #special case

    # A036562 a(n) = 4^(n+1) + 3*2^n + 1.
    i = 0
    while (result := 4**(i+1) + (3*(2**i)+1)) < n:
        gap_seq.append(result)
        i += 1
    
    gap_seq.reverse()

    for gap in gap_seq:
        for i in range(gap,n):
            tmp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > tmp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = tmp 

    return nums
