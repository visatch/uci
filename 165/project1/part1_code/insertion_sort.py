
# Each sorting function should accept a list of integers as the single required
# parameter, as shown below. The input list should be sorted upon completion.
from typing import List

def insertion_sort(nums: List[int]):
	# i = 0
	# while i < len(nums):
	# 	j = i
	# 	while j > 0 and nums[j-1] > nums[j]:
	# 		nums[j], nums[j-1] = nums[j-1],nums[j]
	# 		j = j - 1
	# 	i += 1
	for i in range(len(nums)):
		for j in range(i,0,-1):
			if nums[j-1] > nums[j]:
				nums[j], nums[j-1] = nums[j-1],nums[j]


	return nums




