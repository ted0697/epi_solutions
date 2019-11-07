import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
	min_heap, result = [], []

	for row in sorted_arrays:
		for element in row:
			heapq.heappush(min_heap, element)

	while min_heap:
		smallest = heapq.heappop(min_heap)
		result.append(smallest)

	return result


# Pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
