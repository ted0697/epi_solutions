from test_framework import generic_test
from collections import deque
from collections import namedtuple

def flip_color(x, y, image):
    # TODO - you fill in here.
    Coordinate = namedtuple('Coordinate', ('x', 'y'))
    to_color = (1 if image[x][y] == 0 else 0)
    queue = deque([(Coordinate(x, y))])

    while queue:
    	cur = queue.pop()

    	if (cur.x >= 0 and cur.x < len(image) and cur.y >= 0 and cur.y < len(image[cur.x]) and image[cur.x][cur.y] != to_color):
    		image[cur.x][cur.y] = to_color

	    	for move in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
	    		next_move = Coordinate(cur.x + move[0], cur.y + move[1])
	    		queue.append(next_move)

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
