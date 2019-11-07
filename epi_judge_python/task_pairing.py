import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
	# task_durations.sort()
	# return [
	# 	PairedTasks(task_durations[i], task_durations[~i])
	# 	for i in range(len(task_durations) // 2)
	# ]
	durations = []
	task_durations.sort()
	front, end = 0, len(task_durations) - 1

	while front < end:
		durations.append(PairedTasks(task_durations[front], task_durations[end]))
		front+=1
		end-=1

	return durations


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))
