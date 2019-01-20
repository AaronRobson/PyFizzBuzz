#!/usr/bin/python

import unittest

import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test(self):
        f = fizzbuzz.fizzBuzz
        self.assertEqual(f(1), '1')
        self.assertEqual(f(2), '2')
        self.assertEqual(f(3), 'Fizz')
        self.assertEqual(f(4), '4')
        self.assertEqual(f(5), 'Buzz')
        self.assertEqual(f(15), 'FizzBuzz')


if __name__ == "__main__":
    unittest.main()
