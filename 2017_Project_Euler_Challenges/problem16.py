#==============================================================================
# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?
#==============================================================================

def sumofdigits(num):
    """Sum all of the digits of a certain number"""
    num = str(num)
    soma = 0
    for i in num:
        soma += int(i)
    return soma