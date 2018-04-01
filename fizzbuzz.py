#!/usr/bin/python

from functools import partial

def isDivisible(numerator, denominator):
    return numerator % denominator == 0

def DivisableFuncFactory(denominator):
    return partial(isDivisible, denominator=denominator)

def GenericFuncFactory(conditions):

    def GenericFunc(num):
        output = [value for predicate, value in conditions if predicate(num)]
        if output:
            return ''.join(output)
        else:
            return str(num)

    return GenericFunc

_conditions = [(DivisableFuncFactory(3), 'Fizz'), (DivisableFuncFactory(5), 'Buzz')]
fizzBuzz = GenericFuncFactory(_conditions)

def FizzBuzzLoop(min=1, max=100):
    return map(fizzBuzz, range(min, max+1))

if __name__ == "__main__":
    for line in FizzBuzzLoop():
        print(line)
