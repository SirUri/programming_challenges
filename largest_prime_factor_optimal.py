""""
Print largest prime factor of a number in an optimized manner.
"""
from math import sqrt

def BiggestPrimeFactor_get_optimal(n):
    """Determines the largest prime factor of n in a fast manner"""
    if n == 1:
        return 0
    if n == 2:
        return 2

    print("\tN\t\tDIV")
    print("\t%i\t" % (n))
    while n % 2 == 0:
        max_Factor = 2
        n /= 2
        print("\t%i\t\t%i" % (n, max_Factor))

    for i in range (3, int(sqrt(n))+1, 2):
        while n % i == 0:
            max_Factor = i
            n /= i
            print("\t%i\t\t%i" % (n, max_Factor))

    return max_Factor

def main():
    n = input("Please input a number so we can determine its largest prime factor: ")
    print("Result: %i" % (BiggestPrimeFactor_get_optimal(n)))

main()
