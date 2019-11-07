from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    # TODO - you fill in here.
    if not prices:
    	return 0.0

    s1, s2, s3, s4 = -prices[0], float('-inf'), float('-inf'), float('-inf')

    for i, price in enumerate(prices):
    	s1 = max(s1, -prices[i])
    	s2 = max(s2, s1+prices[i])
    	s3 = max(s3, s2-prices[i])
    	s4 = max(s4, s3+prices[i])

    return max(0.0, s4)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
