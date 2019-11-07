from test_framework import generic_test


def is_binary_tree_bst(root, low_range=float('-inf'), high_range=float('inf')):
    # TODO - you fill in here.
    res, stack, curr = [], ['empty'], root

    while stack:
    	if curr:
    		stack.append(curr)
    		curr = curr.left
    	else:
    		curr = stack.pop()
    		if curr == 'empty':
    			break
    		res.append(curr.data)
    		curr = curr.right

    # print(res)
    for i in range(1, len(res)):
    	if res[i-1] > res[i]:
    		return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
