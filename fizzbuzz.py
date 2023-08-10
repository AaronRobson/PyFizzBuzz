#!/usr/bin/python

from functools import partial


def is_divisible(numerator: int, denominator: int) -> bool:
    return numerator % denominator == 0


def apply_conditions(num: int, conditions) -> str:
    output = ''.join(value for predicate, value in conditions if predicate(num))
    return output if output else str(num)


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
