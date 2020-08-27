#The Fibonacci sequence is defined by the recurrence relation:
#
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import time

def fibupto(n):
    x = 0
    y = 1
    temp = 0
    fib = [1]
    while len(fib) <= n:
        temp = x + y
        x = y
        y = temp
        fib.append(temp)
    return fib

def fibind(n):
    x = 0
    y = 1
    temp = 0
    if n == 1: return 1
    for i in range(n-1):
        temp = x + y
        x = y
        y = temp
    return temp

def countdig(x):
    return len(str(x))

def problem25():
    ind = 0
    x = 1
    while len(str(x)) < 1000:
        ind += 1
        x = fibind(ind)
    return (x, ind)
start = time.time()
x = problem25()
elapsed = time.time() - start
print(x, "obtained in %s seconds" % elapsed)