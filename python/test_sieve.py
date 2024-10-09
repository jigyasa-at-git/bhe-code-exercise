"""
Test suite for the Sieve class.

This script runs unit tests to validate the functionality of the nth_prime method and includes
a fuzzing test to ensure that random primes are correctly generated.

Instructions to run the tests:
1. Clone the Forked Repository:
   git clone https://github.com/jigyasa-at-git/bhe-code-exercise.git
2. Create and activate a virtual environment:
   python -m venv venv
3. Install Dependencies:
   pip install -r requirements.txt
4. Run Tests:
   python -m unittest test_sieve.py

Contributors:
- Jigyasa (https://github.com/jigyasa-at-git)

Libraries:
- sympy for prime checking in fuzz tests
- unittest for unit testing framework
"""


import random
import unittest

import sympy

from sieve import Sieve

class SieveTest(unittest.TestCase):

    def test_sieve_nth_prime(self) -> None:
        sieve = Sieve()
        self.assertEqual(2, sieve.nth_prime(0)) # Total Time taken: 0.000000 seconds ¯\_(ツ)_/¯
        self.assertEqual(71, sieve.nth_prime(19)) # Total Time taken: 0.264271 seconds
        self.assertEqual(541, sieve.nth_prime(99)) # Total Time taken: 0.017035 seconds
        self.assertEqual(3581, sieve.nth_prime(500)) # Total Time taken: 0.034978 seconds
        self.assertEqual(7793, sieve.nth_prime(986)) # Total Time taken: 0.021989 seconds
        self.assertEqual(17393, sieve.nth_prime(2000)) # Total Time taken: 0.026004 seconds
        self.assertEqual(15485867, sieve.nth_prime(1000000)) # Total Time taken: 0.077955 seconds
        self.assertEqual(179424691, sieve.nth_prime(10000000)) # Total Time taken: 0.248547 seconds
        self.assertEqual(2038074751, sieve.nth_prime(100000000)) # Total Time taken: 1.450387 seconds
        self.assertEqual(22801763513, sieve.nth_prime(1000000000)) # Total Time taken: 8.017118 seconds
        self.assertEqual(252097800629, sieve.nth_prime(10000000000)) # Total Time taken: 46.271795 seconds

    def test_sieve_fuzz_nth_prime(self) -> None:
        sieve = Sieve()

        max_range = 1000
        max_no_of_fuzz_tests = 50

        for _ in range (max_no_of_fuzz_tests):
            # Generate a random number to generate prime for
            n = random.randint (0, max_range)

            # Generate prime # for the nth place
            nth_prime_num = sieve.nth_prime(n)

            # Validate the num generate is actually prime
            self.assertTrue(sympy.isprime(nth_prime_num), f"Generated number {nth_prime_num} is not prime")


