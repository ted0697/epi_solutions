from test_framework import generic_test
import heapq

def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    if not sequence or k < 1:
    	return []

    write_ind, currInd = 0, 0
    min_heap, res = [], []

    for _ in range(k):
    	heapq.heappush(min_heap, sequence[currInd])
    	currInd += 1

    # print(min_heap, k)

    while min_heap:
    	smallest = heapq.heappop(min_heap)
    	res.append(smallest)
    	# currInd += 1
    	if currInd >= len(sequence):
    		continue
    	else:
    		heapq.heappush(min_heap, sequence[currInd])
    		currInd += 1

    # print(min_heap)

    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(sequence, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
