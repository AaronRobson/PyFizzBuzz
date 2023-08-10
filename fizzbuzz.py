#!/usr/bin/python

from typing import Iterable
from itertools import count, islice


def fizzbuzz(num: int) -> str:
    output = 'Fizz' * int(num % 3 == 0) + 'Buzz' * int(num % 5 == 0)
    return output if output else str(num)


def fizzbuzz_loop() -> Iterable[str]:
    return map(fizzbuzz, count(1))


def main() -> None:
    for value in islice(fizzbuzz_loop(), 100):
        print(value)


if __name__ == "__main__":
    main()
