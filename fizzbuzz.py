#!/usr/bin/python

def DivisableFuncFactory(divider):
    return lambda num: num % divider == 0

def GenericFuncFactory(conditions):

    def GenericFunc(num):
        output = tuple(value for predicate, value in conditions if predicate(num))
        if output:
            return ''.join(output)
        else:
            return str(num)

    return GenericFunc

_conditions = ((DivisableFuncFactory(3), 'Fizz'), (DivisableFuncFactory(5), 'Buzz'))
fizzBuzz = GenericFuncFactory(_conditions)

def FizzBuzzLoop(min=1, max=100):
    return (fizzBuzz(i) for i in range(min, max+1))

if __name__ == "__main__":
    for line in FizzBuzzLoop():
        print(line)
