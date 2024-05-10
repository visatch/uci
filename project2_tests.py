import requirements

from typing import TypeVar, NamedTuple, Callable
from copy import deepcopy

# Instructions
# Some test cases for the Zi[ZipTree and bin packing algorithms can be found in the main block below.
#
# Note that passing the test cases here does not necessarily mean that your zip tree or algorithms
# are correctly implemented / will pass other cases. It is a good idea to try and create different
# test cases for both.

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class InsertType(NamedTuple):
	key: KeyType
	val: ValType
	rank: int

def create_tree_with_data(data: list[InsertType]) -> requirements.ZipZipTree:
	tree = requirements.ZipZipTree(capacity = len(data))
	for item in data:
		tree.insert(item.key, item.val, item.rank)

	return tree

class ProblemInstance(NamedTuple):
	items: list[float]
	assignments: list[int]
	free_space: list[float]

def is_equal(v1: list[float], v2: list[float]) -> bool:
	for a, b in zip(v1, v2):
		if abs(a - b) > 1e-6:
			return False
	return True

def test_algorithm(test: ProblemInstance, expected_result: ProblemInstance, algorithm: Callable[[list[float], list[int], list[float]], None], name: str):
	test_copy = deepcopy(test)
	algorithm(test_copy.items, test_copy.assignments, test_copy.free_space)

	if test_copy.assignments == expected_result.assignments and is_equal(test_copy.free_space, expected_result.free_space):
		print(f'Test case passed: {name}')
	else:
		print(f'Test case failed: {name}')

def zip_tree_tests():
	print('testing ZipTree')

	data = [InsertType(4, 'a', requirements.Rank(0, 9)), InsertType(5, 'b', requirements.Rank(0, 9)), InsertType(2, 'c', requirements.Rank(1, 12)), InsertType(1, 'd', requirements.Rank(1, 5))]
	tree = create_tree_with_data(data)

	print(f'find(4): {tree.find(4)}, Expected: a')
	print(f'get_size(): {tree.get_size()}, Expected: 4')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 1')
	tree.insert(0, 'e', requirements.Rank(1, 5))
	print(f'get_size(): {tree.get_size()}, Expected: 5')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 2\n')

	data2 = [InsertType(4, 'a', requirements.Rank(2, 1)), InsertType(5, 'b', requirements.Rank(2, 2)), InsertType(2, 'c', requirements.Rank(1, 8)), InsertType(1, 'd', requirements.Rank(0, 12)), InsertType(0, 'e', requirements.Rank(1, 8))]

	tree2 = create_tree_with_data(data2)

	print(f'find(4): {tree2.find(4)}, Expected: a')
	print(f'get_size(): {tree2.get_size()}, Expected: 5')
	print(f'get_height(): {tree2.get_height()}, Expected: 4')
	print(f'get_depth(2): {tree2.get_depth(2)}, Expected: 3')
	print(f'get_depth(1): {tree2.get_depth(1)}, Expected: 4')
	###### my test
	tree2.print_tree()	
	tree2.remove(4)
	print(f'get_size(): {tree2.get_size()}, Expected: 4')
	tree2.print_tree()
	print(f'find(4): {tree2.find(4)}, Expected: a')
	print(f'get_height(): {tree2.get_height()}, Expected: 4')

	print('\ntesting random geometric rank generation')
	geometric_rank_sum = 0
	num_ranks = 10000
	tree3 = requirements.ZipZipTree(capacity = num_ranks)

	for _ in range(num_ranks):
		geometric_rank_sum += tree3.get_random_rank().geometric_rank

	geometric_rank_mean = geometric_rank_sum / num_ranks

	print(f'random geometric rank mean: {geometric_rank_mean}, Expected: ~1')

	# add new tests...

def bin_packing_tests():
	print('\ntesting bin packing\ntest 1')
	items = [0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4]
	assignments = [0] * len(items)
	free_space = list()

	test1 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# # next-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 0, 1, 1, 2, 2, 3, 3], free_space = [0.1, 0.2, 0.1, 0.0])
	# test_algorithm(test1, expected_result, requirements.next_fit, 'next_fit')

	# # first-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 0, 1, 1, 2, 1, 3, 3], free_space = [0.1, 0.0, 0.3, 0.0])
	# test_algorithm(test1, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 2, 1, 0, 3], free_space = [0.0, 0.0, 0.0, 0.4])
	test_algorithm(test1, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# # best-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 0, 1, 1, 2, 1, 3, 3], free_space = [0.1, 0.0, 0.3, 0.0])
	# test_algorithm(test1, expected_result, requirements.best_fit, 'best_fit')

	# # best-fit decreasing
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 2, 1, 0, 3], free_space = [0.0, 0.0, 0.0, 0.4])
	# test_algorithm(test1, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	print('\ntest 2')
	items = [0.79, 0.88, 0.95, 0.12, 0.05, 0.46, 0.53, 0.64, 0.04, 0.38, 0.03, 0.26]
	assignments = [0] * len(items)
	free_space = list()

	test2 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# # next-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6], free_space = [0.21, 0.12, 0.05, 0.37, 0.47, 0.32, 0.33])
	# test_algorithm(test2, expected_result, requirements.next_fit, 'next_fit')

	# # first-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 0, 0, 3, 3, 4, 0, 5, 1, 4], free_space = [0, 0.09, 0.05, 0.01, 0.1, 0.62])
	# test_algorithm(test2, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 4, 5, 3, 1, 0, 2, 2], free_space = [0, 0, 0.14, 0.1, 0.01, 0.62])
	# test_algorithm(test2, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# # best-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 1, 2, 3, 3, 4, 0, 5, 0, 4], free_space = [0.14, 0, 0, 0.01, 0.1, 0.62])
	# test_algorithm(test2, expected_result, requirements.best_fit, 'best_fit')

	# # best-fit decreasing
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 4, 5, 3, 1, 0, 3, 3], free_space = [0, 0, 0.21, 0.03, 0.01, 0.62])
	# test_algorithm(test2, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	print('\ntest 3')
	items = [0.43, 0.75, 0.25, 0.42, 0.54, 0.03, 0.64]
	assignments = [0] * len(items)
	free_space = list()

	test3 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# # next-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 1, 2, 2, 2, 3], free_space = [0.57, 0, 0.01, 0.36])
	# test_algorithm(test3, expected_result, requirements.next_fit, 'next_fit')

	# # first-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 0, 2, 2, 0, 3], free_space = [0.29, 0.25, 0.04, 0.36])
	# test_algorithm(test3, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 2, 3, 0, 1], free_space = [0, 0.33, 0.03, 0.58])
	# test_algorithm(test3, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# # best-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 1, 0, 2, 0, 3], free_space = [0.12, 0, 0.46, 0.36])
	# test_algorithm(test3, expected_result, requirements.best_fit, 'best_fit')

	# # best-fit decreasing
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 2, 3, 0, 2], free_space = [0, 0.36, 0, 0.58])
	# test_algorithm(test3, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	print('\ntest 4')
	items = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
	assignments = [0] * len(items)
	free_space = list()

	test4 = ProblemInstance(items = items, assignments = assignments, free_space = free_space)

	# # next-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9, 9, 10, 11, 11], free_space = [0.46, 0.33, 0.54, 0.14, 0.17, 0.36, 0.5, 0.47, 0.26, 0.03, 0.37, 0.53])
	# test_algorithm(test4, expected_result, requirements.next_fit, 'next_fit')

	# # first-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 0, 2, 1, 1, 3, 4, 5, 1, 5, 6, 2, 4, 2, 6, 3, 7, 8, 3], free_space = [0, 0.01, 0, 0.08, 0.12, 0, 0.01, 0.37, 0.57])
	# test_algorithm(test4, expected_result, requirements.first_fit, 'first_fit')

	# first-fit decreasing
	expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 0, 0, 2, 0, 2], free_space = [0, 0.01, 0.01, 0, 0.14, 0, 0, 0])
	# test_algorithm(test4, expected_result, requirements.first_fit_decreasing, 'first_fit_decreasing')

	# # best-fit
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 0, 2, 1, 1, 3, 4, 5, 1, 5, 6, 4, 6, 3, 2, 3, 7, 8, 3], free_space = [0, 0.01, 0.18, 0.01, 0, 0, 0.02, 0.37, 0.57])
	# test_algorithm(test4, expected_result, requirements.best_fit, 'best_fit')

	# # best-fit decreasing
	# expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 2, 4, 4, 0, 4], free_space = [0.13, 0.01, 0.02, 0, 0, 0, 0, 0])
	# test_algorithm(test4, expected_result, requirements.best_fit_decreasing, 'best_fit_decreasing')

	# add new tests...

if __name__ == '__main__':
	# zip_tree_tests()
	bin_packing_tests()
