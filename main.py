def factorials(n):
    if n < 0 or n != int(n):
        raise ValueError


    factorial = 1
    if n == 0:
        yield factorial
    else:
        for i in range(1, n + 1):
            factorial *= i
            yield factorial


def main():
    for i, factorial in enumerate(factorials(100)):
        print(f"{i + 1}! = {factorial}")


if __name__ == "__main__":
    main()
