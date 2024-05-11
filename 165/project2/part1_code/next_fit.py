# Example file: next_fit.py

# explanations for member functions are provided in requirements.py

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
	bin_capacity = 1
	bin_index = 0
	free_space.append(bin_capacity)

	for i,item in enumerate(items):
		if free_space[bin_index] >= item - 1e-12:
			assignment[i] = bin_index
			free_space[bin_index] -= item
		else:
			bin_index += 1
			free_space.append(bin_capacity - item)
			assignment[i] = bin_index