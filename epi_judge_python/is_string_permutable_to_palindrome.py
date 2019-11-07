from test_framework import generic_test
from collections import Counter

def can_form_palindrome(s):
    # TODO - you fill in here.
    s_map = Counter(s)
    count = 0
    for k in s_map:
    	if (s_map[k] % 2 != 0):
    		count += 1
    		if count > 1:
    			return False

    return True
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
