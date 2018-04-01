#!/usr/bin/python

def DivisableFuncFactory(divider):
    return lambda num: num % divider == 0

def GenericFuncFactory(conditions):
    #Must evaluate generators as otherwise function will only work the first time; after which the generator will be finished.
    conditions = tuple(conditions)

    def GenericFunc(num):
        output = tuple(value for predicate, value in conditions if predicate(num))
        if output:
            return ''.join(output)
        else:
            return str(num)

    return GenericFunc

_dividerConditions = ((3, 'Fizz'), (5, 'Buzz'))
_conditions = ((DivisableFuncFactory(predicateNum), value) for predicateNum, value in _dividerConditions)
fizzBuzz = GenericFuncFactory(_conditions)

def FizzBuzzLoop(min=1, max=100):
    return (fizzBuzz(i) for i in range(min, max+1))

if __name__ == "__main__":
    for line in FizzBuzzLoop():
        print(line)
