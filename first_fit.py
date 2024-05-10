from typing import List
from zipzip_tree_ff import ZipZipTreeFF, FFVal
from hybrid_sort import hybrid_sort
from decimal import *

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    getcontext().prec = 6
    bin_tree = ZipZipTreeFF(len(items))
    bin_capacity = Decimal(1.0)
    bin_index = 0 

    for i, item in enumerate(items):
        item = Decimal(str(item))
        best_bin = bin_tree.find_best_fit(item)

        if best_bin is None:
            new_bin_val = FFVal(remaining_capacity = bin_capacity - item, best_remaining_capacity = bin_capacity - item)
            bin_tree.insert(bin_index, new_bin_val, bin_tree.get_random_rank())
            assignment[i] = bin_index

            new_bin_free_space = bin_capacity - item
            free_space.append(float(new_bin_free_space))

            bin_index += 1
        else:
            assignment[i] = best_bin.key
            best_bin.val.remaining_capacity = best_bin.val.remaining_capacity - item

            free_space[best_bin.key] = float(best_bin.val.remaining_capacity)
            bin_tree.update_tree(best_bin.key)


def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    items = hybrid_sort(items,0)
    first_fit(items, assignment, free_space)
    print(assignment)
    print(free_space) 