#!/usr/bin/python

import unittest
from itertools import islice

import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test(self):
        f = fizzbuzz.fizzbuzz
        self.assertEqual(f(1), '1')
        self.assertEqual(f(2), '2')
        self.assertEqual(f(3), 'Fizz')
        self.assertEqual(f(4), '4')
        self.assertEqual(f(5), 'Buzz')
        self.assertEqual(f(15), 'FizzBuzz')


class TestFizzBuzzLoop(unittest.TestCase):

    def test(self):
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
        ]
        actual = take(len(expected), fizzbuzz.fizzbuzz_loop())
        self.assertEqual(expected, actual)


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


if __name__ == "__main__":
    unittest.main()
