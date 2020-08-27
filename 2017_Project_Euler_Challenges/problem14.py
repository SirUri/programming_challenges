#==============================================================================
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
#  that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
#==============================================================================
import time

def seq14(n):
    """Generates the sequence provided for the problem 14.
    "n" is the starting point"""
    seq = [n]
    while n != 1:
        if n%2 == 0:
            n /= 2
            seq.append(n)
        elif n%2 != 0:
            n = 3*n + 1
            seq.append(n)
    return seq

def problem14():
    maior = len(seq14(1))
    for i in range(10,1000001):
        x = len(seq14(i))
        if x > maior:
            num = i
            maior = x
    return maior, num
start = time.clock()
print(problem14())
stop = time.clock()
print(stop - start)