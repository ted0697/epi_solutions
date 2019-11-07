from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.    
    result_list = dummy = ListNode()

    while L1 and L2:
    	if L1.data < L2.data:
    		result_list.next = L1
    		L1 = L1.next
    	else:
    		result_list.next = L2
    		L2 = L2.next

    	result_list = result_list.next

    if L1:
    	result_list.next = L1
    else:
    	result_list.next = L2

    return dummy



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
