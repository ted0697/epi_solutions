from test_framework import generic_test


def gcd(x, y):
    # TODO - you fill in here.

    # if x > y and y != 0:
    # 	x,y,y,x
    # if y == 0:
    # 	return x
    # else:
    # 	return gcd(y, x%y)

    print(x,y)
    while y != 0:
    	temp = y
    	y = x%y
    	x = temp
    print(x, 'return')
    return x
    


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
