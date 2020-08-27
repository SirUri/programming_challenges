#==============================================================================
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
#  without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers
#  from 1 to 20?
# 
#==============================================================================

def problem5(num):
    AllDiv = False
    x = num
    while not AllDiv:
        for i in range(1,x+1):
            if num % i != 0:
                num += x
                break
            if i == x:
                AllDiv = True
    return num

problem5(20)
            
            
            