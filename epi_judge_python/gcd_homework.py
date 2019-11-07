def gcd_recursive(x,y):
    if x > y and y != 0:
    	x,y,y,x
    if y == 0:
    	return x
    else:
    	return gcd_recursive(y, x%y)

def gcd_iter(x,y):
	if x > y and y != 0:
		x,y = y,x

	while y != 0:
		temp = y
		y = x % y
		x = temp

	return x


def main():

	test_cases = [[448, 3019243], [113650310, 117230], [28, 1890], [147155, 6305], [900,9450285], [14, 37547090], [718749539, 7636], [10,45],[1701,3768]]
	expected_results = [1, 10, 14, 5, 15, 14, 83, 5, 3]


	print('GCD Recursion Test Cases')
	print('------------------------\n')

	for i, case in enumerate(test_cases):
		result = gcd_recursive(case[0], case[1])
		print('Expected: ' + str(expected_results[i]) + ' ----- Result: ' + str(result))
		if result == expected_results[i]:
			print('***PASSED***')
		else:
			print('***FAILED***') 
		print('')

	print('GCD Ierative Test Cases')
	print('------------------------\n')

	for i, case in enumerate(test_cases):
		result = gcd_iter(case[0], case[1])
		print('Expected: ' + str(expected_results[i]) + ' ----- Result: ' + str(result))
		if result == expected_results[i]:
			print('***PASSED***')
		else:
			print('***FAILED***') 
		print('')

main()
