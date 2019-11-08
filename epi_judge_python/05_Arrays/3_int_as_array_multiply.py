from test_framework import generic_test


def multiply(num1, num2):
	# TODO - you fill in here.
	res = 0
	carry = 0
	i = 0
	for num_2 in reversed(num2):
		temp = []
		for num_1 in reversed(num1):
			mult_res = num_2 * num_1 + carry
			if mult_res >= 10:
				temp.append(mult_res % 10)
				carry = mult_res // 10
			else:
				temp.append(mult_res)
				carry = 0
		if i >= 1:
			val = int("".join(temp)) * 10 * i
			res += val
		else:
			val = int("".join(temp))
			res += val

		i += 1
	print(res)
	return [str(x) for x in str(res)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
