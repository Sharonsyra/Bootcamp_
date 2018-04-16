import unittest
from prime_numbers_list import *
#test

class PrimesTestCase(unittest.TestCase):
    def test_four_not_in_list(self):
        result = primes(7)
        self.assertNotIn(4, result)

    def test_two_is_a_prime_number(self):
        result = primes(9)
        self.assertIn(2, result)

    def test_thirteen_is_in_the_result(self):
        result = primes(13)
        self.assertIn(13, result)

    def test_length_of_list_less_than_n(self):
        self.assertLess(len(primes(9)), 9)
   
    def test_ninety_seven_is_a_prime(self):
        result = primes(100)
        self.assertIn(97, result)

    def test_sixty_seven_is_a_prime(self):
        result = primes(97)
        self.assertIn(67, result)

    def test_seventy_two_is_not_a_prime_number(self):
        result = primes(75)
        self.assertNotIn(72, result)

    def test_output_is_a_list(self):
        result = primes(43)
        result = isinstance(result, list)
        self.assertTrue(result)

    def test_one_returns_an_empty_list(self):
        result = primes(1)
        self.assertNotIn(1, result)

    def test_return_empty_list_if_n_is_negative(self):
        result = primes(-3)
        self.assertListEqual([],result)

    def test_raise_error_if_input_is_not_integer(self):
    	with self.assertRaises(TypeError):
    		primes('string')


if __name__ == '__main__':
    unittest.main()

