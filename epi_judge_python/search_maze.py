import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import deque

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    # TODO - you fill in here.

    # stack = deque([s])

    # visited = {}
    # path = []

    # while stack:
    #     curr = stack.popleft()
    #     #go through all the moves
    #     path.append(curr)
    #     maze[curr.x][curr.y] = BLACK
    #     for move in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #         next_node = Coordinate(curr.x + move[0], curr.y + move[1])

    #         if not (next_node.x >= 0 and next_node.x < len(maze) and next_node.y >= 0 and next_node.y < len(maze[next_node.x]) and maze[next_node.x][next_node.y] == WHITE):
    #             continue
    #         else:
    #             if next_node == e:

    #                 return next_node
    #             stack.append(next_node)

    # return []


    def search_maze_helper(cur):
        if not (cur.x >= 0 and cur.x < len(maze) and cur.y >= 0 and cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False

        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        results = [search_maze_helper(Coordinate(cur.x - 1, cur.y)), search_maze_helper(Coordinate(cur.x + 1, cur.y)),
        search_maze_helper(Coordinate(cur.x, cur.y - 1)), search_maze_helper(Coordinate(cur.x, cur.y + 1))]

        for result in results:
            if result:
                return True

        path.pop()
        return False

    path = []
    if not search_maze_helper(s):
        return []
    return path
    #181, 64


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))
    # print(path, 'path')
    # print(e, 'e')
    # return path == e
    # print(s, 's')
    # print(e, 'e')
    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
