from test_framework import generic_test


def plus_one(A):
	carry = 1
	for i in range(len(A)-1, -1, -1):
		# add_res = A[i] + carry
		A[i] += carry

		if A[i] == 10:
			A[i], carry = 0, 1
		else:
			carry = 0
			break

	if carry == 1:
		A = [1] + A

	return A





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
