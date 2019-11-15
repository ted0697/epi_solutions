from test_framework import generic_test


def apply_permutation(perm, A):
    # TODO - you fill in here.
	i = 0
	while i < len(A):
		if perm[i] != i:
			A[i], A[perm[i]] = A[perm[i]], A[i]
			ind, ind2 = i, perm[i]
			perm[ind], perm[ind2] = perm[ind2], perm[ind]
		else:
			i += 1

	return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
