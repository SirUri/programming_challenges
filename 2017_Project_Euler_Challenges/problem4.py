#==============================================================================
# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
#==============================================================================

def ispalindromenum(x):
    """Determines if x is a palindrome number"""
    return str(x) == str(x)[::-1]

def problem4_2dig():
    z = 0
    for i in range(10,100):
        for j in range(10,100):
            if ispalindromenum(j*i):
                if i*j > z:
                    z = i*j
    return z

problem4_2dig()

def problem4_3dig():
    z = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            if ispalindromenum(i*j):
                if i*j > z:
                    z = i*j
    return z

problem4_3dig()
