#==============================================================================
# Starting in the top left corner of a 2×2 grid, and only being able to move to the 
# right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
#==============================================================================
#http://mathforum.org/library/drmath/view/66728.html
from math import factorial

def combination(columns, rows):
    path = columns + rows
    c = (factorial(path))/((factorial(rows))*factorial(path - rows))
    return c

answer = combination(20,20)