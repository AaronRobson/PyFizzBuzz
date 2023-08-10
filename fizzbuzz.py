#!/usr/bin/python


def fizzbuzz(num: int) -> str:
    output = ('Fizz' if num % 3 == 0 else '') + ('Buzz' if num % 5 == 0 else '')
    return output if output else str(num)


def fizzbuzz_loop(min=1, max=100):
    return map(fizzbuzz, range(min, max+1))


if __name__ == "__main__":
    for line in fizzbuzz_loop():
        print(line)
