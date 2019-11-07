from test_framework import generic_test


def plus_one(A):

	A[-1] += 1

	for x in range(len(A)-1, 0, -1):
		if A[x] != 10:
			break
		else:
			A[x] = 0
			A[x - 1] += 1

	if A[0] == 10:
		A[0] = 1
		A.append(0)

	return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
