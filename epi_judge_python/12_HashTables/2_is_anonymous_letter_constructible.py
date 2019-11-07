from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    r = Counter(letter_text)
    m = Counter(magazine_text)
    
    for c in letter_text:
        if r[c] <= m[c]:
            continue
        else:
            return False
    return True
        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
