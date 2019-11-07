from test_framework import generic_test
from collections import Counter

def has_three_sum(A, t):
    int_map = Counter(A)
    A.sort()

    l_ptr, r_ptr, e_ptr = 0, 0, len(A)

    while l_ptr < e_ptr:

    	while r_ptr < e_ptr:
    		two_sum = A[l_ptr] + A[r_ptr]

    		complement = t - two_sum
    		if complement in int_map:
    			return True
    		r_ptr = r_ptr + 1

    	l_ptr = l_ptr + 1
    	r_ptr = l_ptr

    return False


# has_three_sum([1,-1], 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
