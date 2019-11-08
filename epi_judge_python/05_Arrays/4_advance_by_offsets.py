from test_framework import generic_test


def can_reach_end(A):
    # TODO - you fill in here.

    jump_dist = 0

    for ind, num in enumerate(A):
    	jump_dist = max(jump_dist, num + ind)
    	if jump_dist >= len(A) - 1:
    		return True
    	if ind >= jump_dist:
    		return False
    #book solution -- more elegant
    # furthest_reach, last_ind = 0, len(A) - 1
    # i = 0
    # while i <= furthest_reach and furthest_reach < last_ind:
    # 	furthest_reach = max(furthest_reach, A[i] + i)
    # 	i += 1
    # return furthest_reach >= last_ind
    # if len(A) == 1:
    # 	return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
