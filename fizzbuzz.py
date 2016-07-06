#!/usr/bin/python

def DivisableFuncFactory(divider):
  def Divisable(num):
    '''Is number divisable by %d?
    ''' % divider
    return num % divider == 0
  return Divisable

def GenericFuncFactory(conditions, sep=None, allMatches=True):
  #Must evaluate generators as otherwise function will only work the first time; after which the generator will be finished.
  conditions = tuple(conditions)

  if sep == None:
    sep = ''

  def GenericFunc(num):
    output = tuple(value for predicate, value in conditions if predicate(num))
    if output:
      if allMatches:
        return sep.join(output)
      else:
        return output[0]
    else:
      return num

  return GenericFunc

def FizzBuzzFunc(sep=None):
  dividerConditions = ((3, 'Fizz'), (5, 'Buzz'))
  conditions = ((DivisableFuncFactory(predicateNum), value) for predicateNum, value in dividerConditions)
  return GenericFuncFactory(conditions, sep)

def GenericLoop(func, min, max, step=1):
  min, max = sorted([min, max])
  return (func(i) for i in range(min, max+1, step))

def FizzBuzzLoop(min=1, max=100, sep=None):
  return GenericLoop(FizzBuzzFunc(sep), min, max)

if __name__ == "__main__":
  for line in FizzBuzzLoop():
    print(line)
  input('\nPress Enter to Close:')
