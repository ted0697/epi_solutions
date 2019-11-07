from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
	a,b, write_ind = m-1, n-1, m + n -1

	while a >= 0 and b >= 0:
		if A[a] > B[b]:
			A[write_ind] = A[a]
			a -= 1
		else:
			A[write_ind] = B[b]
			b -= 1

		write_ind -= 1

	while b >= 0:
		A[write_ind] = B[b]
		write_ind, b = write_ind - 1, b - 1

	return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
