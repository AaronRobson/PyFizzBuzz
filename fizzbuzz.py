#!/usr/bin/python3


def fizzbuzz(num: int) -> str:
    return ('Fizz' * int(num % 3 == 0) + 'Buzz' * int(num % 5 == 0)) or str(num)


def main() -> None:
    for value in range(1, 100 + 1):
        print(fizzbuzz(value))


if __name__ == "__main__":
    main()
