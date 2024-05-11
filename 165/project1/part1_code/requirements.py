# Import each one of your sorting algorithms below as follows:
# Feel free to comment out these lines before your algorithms are implemented.
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
from hybrid_sort import hybrid_sort1, hybrid_sort2, hybrid_sort3

# Please read the below carefully:

# - Each sorting algorithm should be implemented in its own file.
# - No file should include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - Each function should modify the input list so that it is sorted upon completion.

# Note:
#   If your Shellsort and/or hybrid merge sort variants largely use the same code,
#   you may choose to implement them in a single file, and import them as follows:
# from shell_sort import shell_sort1, shell_sort2, shell_sort3, shell_sort4
# from hybrid_sort import hybrid_sort1, hybrid_sort2, hybrid_sort3

# l = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
# print(insertion_sort(l))