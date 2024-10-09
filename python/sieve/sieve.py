import math

import sympy

class Sieve:

    def __init__(self) -> None:
        pass

    def nth_prime(self, n: int) -> int:
        return sympy.prime (n+1) # sympy is 1 based index hence n+1

    """
    These are 2 other functions which are not efficient.
    I was not able to get the prime value even for 10000000th position from either methods
    """

    def nth_prime_basic(self, n):
        # Chk if num is prime
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Prime number counter
        count = 0
        prime_num = 1

        # Loop to find the nth prime
        while count <= n:
            prime_num += 1
            if is_prime(prime_num):
                count += 1
        return prime_num


    def nth_prime_soe(self, n):
        # Return 2 for the 0th position per the assignment
        if n == 0:
            return 2

        # Estimate an upper limit to for the rage using Prime number theorem
        # (gives a rough estimate of the upper bound for the nth prime)
        upper_limit = int(n * math.log(n) + n * math.log(math.log(n))) + 10

        # Boolean array w 'upper_limit' as size of the array
        sieve = [True] * (upper_limit + 1)
        sieve[0], sieve[1] = False, False

        prime_list = []

        # Mark multiples of each prime starting from 2 (based on Sieve of Eratosthenes)
        for p in range(2, upper_limit + 1):
            if sieve[p]:
                prime_list.append(p)
                for multiple in range(p * p, upper_limit + 1, p):
                    sieve[multiple] = False

            # Since we have gustimated the Range of numbers based on 'n',
            # we have to break out of the loop if we get more than 'n' primes
            if len(prime_list) > n:
                break

        return prime_list[n]
