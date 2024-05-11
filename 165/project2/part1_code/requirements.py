# Import each one of your sorting algorithms below as follows:
# Feel free to comment out these lines before your algorithms are implemented.
from next_fit import next_fit
from first_fit import first_fit
from first_fit import first_fit_decreasing
from best_fit import best_fit
from best_fit import best_fit_decreasing
from zipzip_tree import ZipZipTree, Rank

# Details about Gradescope submission:

# - Next-fit, first-fit, and best-fit algorithms should be stored in separate files.
# - No file should include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - The submission should either be the files themselves, or a zip file not containing any directories.

# Note: The provided code use features from Python 3.9+, feel free to remove them if using an earlier version of Python.
#       It is recommended for you to use Python 3.10 or Python 3.11 to test your code.
#       Both versions are available on OpenLab, perhaps requiring a module load (e.g., module load python/3.10).

# Explanations for ZipZipTree public member functions:

# any variable annotated with KeyType should use the same type for each tree, and should be comparable.
# ValType is for any additional data to be stored in the nodes.
# Rank is a container representing each node's rank, both geometric and uniform.
#           If using an earlier form of Python, you can use a named tuple instead.
# ZipZipTree(): constructs the zip-zip tree with a specific capacity.
# get_random_rank(): returns a random node rank, chosen independently from:
#           a geometric distribution of mean 1 and,
#           a uniform distribution of integers from 0 to log(capacity)^3 - 1 (log capacity cubed minus 1).
# insert(): inserts item with parameter key, value, and rank into tree.
#           if rank is not provided, a random rank should be selected by using get_random_rank().
# remove(): removes item with parameter key from tree.
#           you can assume that the item exists in the tree.
# find(): returns the value of item with parameter key.
#         you can assume that the item exists in the tree.
# get_size(): returns the number of nodes in the tree.
# get_height(): returns the height of the tree.
# get_depth(): returns the depth of the item with parameter key.
#              you can assume that the item exists in the tree.


# For all bin packing functions:
# params:
# 	items: the items to assign to the bins
# 	assignment: the assignment of the ith item to the jth bin for all i items.
# 	            bin numbers start from 0.
# 	            assume len(assignment) == len(items).
# 	            you should not add any new elements to this list.
# 	            you must modify this list's elements to indicate the assignment.
# 	            see comment below for first-fit decreasing and for best-fit decreasing.
#
# 	free_space: the amount of space left in the jth bin for all j bins created by the algorithm.
# 	            you should add one element for each bin that the algorithm creates.
# 	            when the function returns, this should indicate the final free space available in each bin.

# For first-fit decreasing and best-fit decreasing:
# The assignment list argument should refer to item indices *after* sorting.
# You don't need to map the assignment indices in some clever way.
# As such, the assignments list for these algorithms will have little practical usage other than testing.
