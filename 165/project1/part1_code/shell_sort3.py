from typing import List

def shell_sort3(nums: List[int]):
    n = len(nums)
    gap_seq = set()
    # gap_seq = [67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    #A003586 3-smooth numbers: numbers of the form 2^i*3^j with i, j >= 0

    i = 0
    while (2**i) < n:
        j = 0
        while (value := 2**i * 3**j) < n:
            gap_seq.add(value)
            j += 1
        i += 1
    
    gap_seq = sorted(gap_seq,reverse=True)
    print(gap_seq)

    for gap in gap_seq:
        for i in range(gap,n):
            tmp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > tmp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = tmp 

    return nums

# l = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
# print(shell_sort3(l))