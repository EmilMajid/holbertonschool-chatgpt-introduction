#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given integer n using recursion.
    The factorial of a number n (denoted as n!) is the product of all positive integers
    less than or equal to n. The factorial of 0 is defined as 1.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input number n.
           - If n is 0, returns 1 (by definition of 0!).
           - Otherwise, returns n multiplied by the factorial of n-1, computed recursively.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the input number from command line argument
f = factorial(int(sys.argv[1]))

# Output the result (factorial of the number)
print(f)

