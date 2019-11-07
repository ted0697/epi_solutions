from test_framework import generic_test


def search_smallest(A):
    # TODO - you fill in here.
	if not A:
		return -1

	left, right, mid = 0, len(A) - 1, 0

	while left < right:
		mid = (left + right) // 2
		target = A[mid]

		if target < A[right]:
			right = mid
		else:
			left = mid + 1
	
	return left



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
