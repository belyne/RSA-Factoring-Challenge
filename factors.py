#!/usr/bin/python3
import sys

def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r") as file:
        for line in file:
            number = int(line.strip())
            factorizations = factorize(number)
            for factors in factorizations:
                p, q = factors
                print(f"{number}={p}*{q}")
