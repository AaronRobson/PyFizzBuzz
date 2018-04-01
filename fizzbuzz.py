#!/usr/bin/python

from functools import partial

def isDivisible(numerator, denominator):
    return numerator % denominator == 0

def ApplyConditions(num, conditions):
    output = [value for predicate, value in conditions if predicate(num)]
    if output:
        return ''.join(output)
    else:
        return str(num)

_conditions = [
    (partial(isDivisible, denominator=3), 'Fizz'),
    (partial(isDivisible, denominator=5), 'Buzz')
]
fizzBuzz = partial(ApplyConditions, conditions=_conditions)

def FizzBuzzLoop(min=1, max=100):
    return map(fizzBuzz, range(min, max+1))

if __name__ == "__main__":
    for line in FizzBuzzLoop():
        print(line)
