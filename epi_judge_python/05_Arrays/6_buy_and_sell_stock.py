from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    curr_max = float('-inf')
    if not prices:
    	return 0.0
    min_stock = prices[0]

    for price in prices:
    	if price < min_stock:
    		min_stock = price
    	else:
    		gain = price - min_stock
    		curr_max = max(gain, curr_max)

    return curr_max


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
