from typing import List

def hybrid_sort(nums: List[int],H :int) -> List[int]:
    n = len(nums)

    if n > H:
        mid = n // 2
        L = nums[:mid]
        R = nums[mid:]

        hybrid_sort(L,H)
        hybrid_sort(R,H)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
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
                if nums[j-1] > nums[j]:
                    nums[j],nums[j-1] = nums[j-1], nums[j]

    return nums

def hybrid_sort1(nums: List[int]) -> List[int]:
    H = len(nums) ** (1/5)
    return hybrid_sort(nums,H)

def hybrid_sort2(nums: List[int]) -> List[int]:
    H = len(nums) ** (2/5)
    return hybrid_sort(nums,H)

def hybrid_sort3(nums: List[int]) -> List[int]:
    H = len(nums) ** (3/5)
    return hybrid_sort(nums,H)

# l = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
# print(hybrid_sort3(l))