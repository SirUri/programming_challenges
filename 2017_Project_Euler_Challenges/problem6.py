#==============================================================================
# The sum of the squares of the first ten natural numbers is,
# 
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.
#==============================================================================
#Problem 6

def sumofsquares(n):
    """This will return the sum of the squares of the first n natural numbers"""
    soma = 0
    for i in range(1,n+1):
        soma += i**2
    return soma

sumofsquares(10)

def squareofsum(n):
    """Returns the square of the sum of the first n natural numbers"""
    soma = 0
    for i in range(1,n+1):
        soma += i
    return soma**2

squareofsum(10)

squareofsum(100) - sumofsquares(100)