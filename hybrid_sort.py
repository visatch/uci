from typing import List

def hybrid_sort(nums: List[int],H: int) -> List[int]:
    H = len(nums) ** (2/5)
    n = len(nums)

    if n > H:
        mid = n // 2
        L = nums[:mid]
        R = nums[mid:]

        hybrid_sort(L,H)
        hybrid_sort(R,H)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
        
    else:
        for i in range(len(nums)):
            for j in range(i,0,-1):
                if nums[j-1] < nums[j]:
                    nums[j],nums[j-1] = nums[j-1], nums[j]
    
    return nums


