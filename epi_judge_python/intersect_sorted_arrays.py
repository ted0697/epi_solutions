from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    i, j = 0, 0
    res = []

    while i < len(A) and j < len(B):
    	if A[i] == B[j]:
    		if i == 0 or A[i] != A[i - 1]:
    			res.append(A[i])
    		i, j = i + 1, j + 1
    	elif A[i] < B[j]:
    		i += 1
    	else:
    		j += 1
 

    return res





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
