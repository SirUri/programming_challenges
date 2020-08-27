#==============================================================================
# What is the greatest product of four adjacent numbers in the same direction (up,
# down, left, right, or diagonally) in the 20×20 grid?
#==============================================================================



import numpy as np
a = np.loadtxt("problem11.txt")
#Como a matriz é positiva, o maior valor iniciará em zero
def greatestprodhorizontal(a):
    maior = 0
    for i in range(20):
        for j in range(17):
            x = a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]
            if x > maior:
                maior = x
    return maior

def greatestprodvertical(a):
    maior = 0
    for j in range(20):
        for i in range(17):
            x = a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j]
            if x > maior:
                maior = x
        
    return maior

def greatestproddiagonal(M):
    max_prod = 0
    for i in range(16):
        for j in range(16):
            prod = M[i][j]*M[i+1][j+1]*M[i+2][j+2]*M[i+3][j+3]
            if prod > max_prod: max_prod = prod
    for i in range(3,20):
        for j in range(16):
            prod = M[i][j]*M[i-1][j+1]*M[i-2][j+2]*M[i-3][j+3]
            if prod > max_prod: max_prod = prod
    return max_prod

greatestproddiagonal(a)

def biggest(a):
    l = []
    l.append(greatestprodhorizontal(a))
    l.append(greatestprodvertical(a))
    l.append(greatestproddiagonal(a))
    return max(l)
    