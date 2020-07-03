#!/usr/bin/python

from functools import partial


def is_divisible(numerator, denominator):
    return numerator % denominator == 0


def apply_conditions(num, conditions):
    output = [value for predicate, value in conditions if predicate(num)]
    if output:
        return ''.join(output)
    else:
        return str(num)


_conditions = [
    (partial(is_divisible, denominator=3), 'Fizz'),
    (partial(is_divisible, denominator=5), 'Buzz')
]
fizzbuzz = partial(apply_conditions, conditions=_conditions)


def fizzbuzz_loop(min=1, max=100):
    return map(fizzbuzz, range(min, max+1))


if __name__ == "__main__":
    for line in fizzbuzz_loop():
        print(line)
