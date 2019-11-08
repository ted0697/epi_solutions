import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    # TODO - you fill in here.
    for i in range(len(A) - 1):
    	if A[i] == A[i + 1]:
    		A[i] = None

    swap_ind = 0

    for i in range(len(A)):
    	if A[i] != None:
    		A[i], A[swap_ind] = A[swap_ind], A[i]
    		swap_ind += 1

    return swap_ind

    #more elegant + 1 pass solution from textbook
    # if not A:
    # 	return 0

    # write_ind = 1
    # for i in range(1, len(A)):
    # 	if A[write_ind-1] != A[i]:
    # 		A[write_ind] = A[i]
    # 		write_ind += 1
    # return write_ind



@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
