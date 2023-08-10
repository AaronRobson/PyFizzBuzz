#!/usr/bin/python


def fizzbuzz(num: int) -> str:
    output = 'Fizz' * int(num % 3 == 0) + 'Buzz' * int(num % 5 == 0)
    return output if output else str(num)


def fizzbuzz_loop(min=1, max=100):
    return map(fizzbuzz, range(min, max+1))


if __name__ == "__main__":
    for line in fizzbuzz_loop():
        print(line)
