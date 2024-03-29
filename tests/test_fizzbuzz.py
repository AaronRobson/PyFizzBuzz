#!/usr/bin/python3

import unittest
from unittest.mock import call, patch

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


class TestMain(unittest.TestCase):
    @patch('fizzbuzz.print')
    def test(self, mock_patch):
        self.assertIsNone(fizzbuzz.main())
        self.assertEqual(mock_patch.call_args_list[0], call('1'))
        self.assertEqual(mock_patch.call_args_list[1], call('2'))
        self.assertEqual(mock_patch.call_args_list[2], call('Fizz'))
        self.assertEqual(mock_patch.call_args_list[3], call('4'))
        self.assertEqual(mock_patch.call_args_list[4], call('Buzz'))
        self.assertEqual(mock_patch.call_args_list[14], call('FizzBuzz'))
        self.assertEqual(mock_patch.call_count, 100, mock_patch.call_args_list)


if __name__ == "__main__":
    unittest.main()
