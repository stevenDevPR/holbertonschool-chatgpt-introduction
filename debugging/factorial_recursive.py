#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given integer using recursion.
    
    Function Description:
    ---------------------
    This function calculates the factorial of a given integer using recursion.
    Factorial of a non-negative integer n is the product of all positive integers
    less than or equal to n. For example, the factorial of 5 (written as 5!) is
    calculated as 5 * 4 * 3 * 2 * 1 = 120.

    Parameters:
    -----------
    n : int
        The integer for which the factorial needs to be calculated.

    Returns:
    --------
    int
        The factorial of the input integer n.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Parsing command line argument and calculating factorial
f = factorial(int(sys.argv[1]))
print(f)
