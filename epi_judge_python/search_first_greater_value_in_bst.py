from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    # TODO - you fill in here.
    subtree, best_so_far = tree, None

    while subtree:
    	if subtree.data > k:
    		best_so_far, subtree = subtree, subtree.left
    	else:
    		subtree = subtree.right

    return best_so_far


    # stack, curr, pre = ['empty'], tree, None

    # while True:
    # 	if curr:
    # 		stack.append(curr)
    # 		# pre = curr
    # 		curr = curr.left
    # 	else:
    # 		curr = stack.pop()
    # 		if curr == 'empty':
    # 			break
    # 		elif curr.data > k:
    # 			return curr
    # 		else:
    # 			curr = curr.right

    # return None


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
