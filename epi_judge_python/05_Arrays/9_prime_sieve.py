from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
	res = []
	is_prime = [False, False] + [True] * (n-1)

	for i in range(len(is_prime)):
		if is_prime[i]:
			res.append(i)

			for j in range(i, len(is_prime), i):
				is_prime[j] = False
	return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
