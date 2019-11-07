from test_framework import generic_test


def search_first_of_k(A, k):
    # TODO - you fill in here.
    if not A:
    	return -1
    	
    left, right = 0, len(A) - 1

    while left < right:
    	mid = (left + right) // 2
    	if A[mid] >= k:
    		right = mid
    	else:
    		left = mid+1

    if A[left] == k:
    	return left
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
