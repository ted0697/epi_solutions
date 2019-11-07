from test_framework import generic_test, test_utils
from collections import deque

def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    res, stack, curr = [], ['empty'], tree
    end = []

    while True:
    	if curr:
    		stack.append(curr)
    		curr = curr.right
    	else:
    		curr = stack.pop()
    		if curr == 'empty':
    			break
    		end.append(curr.data)
    		k -= 1
    		if k == 0:
    			return end
    		curr = curr.left
    return end




    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
