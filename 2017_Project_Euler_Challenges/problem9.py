#==============================================================================
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#==============================================================================
#problem 9

def istriplet(a,b,c):
    if a != 0 and b != 0 and c != 0:
        return a**2 + b**2 == c**2
    return False

def problem9():
    for a in range(1,1001):
        for b in range(a+1, a+1001):
            if a + b > 1000:
                break
            c = 1000 - a - b
            if istriplet(a,b,c):
                if a + b + c == 1000:
                    return(a*b*c, a, b, c)
problem9()