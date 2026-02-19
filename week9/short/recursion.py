# Current code (kept as requested)
# finding factorial
#
# def factorial(n: int) -> int:
#     if n == 1 or n==0:
#         return 1
#
#     return n * factorial(n-1)
#
# factorial(4)


def countdown(n: int) -> None:
    if n == 0:
        print("Done")
        return
    print(n)
    countdown(n - 1)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def sum_list(values: list[int]) -> int:
    if not values:
        return 0
    return values[0] + sum_list(values[1:])


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci index cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    print("Countdown from 3")
    countdown(3)

    print("\nFactorial")
    print("factorial(4) =", factorial(4))

    print("\nSum list")
    print("sum_list([1, 2, 3, 4]) =", sum_list([1, 2, 3, 4]))

    print("\nFibonacci")
    print("fibonacci(6) =", fibonacci(6))


if __name__ == "__main__":
    main()
