#==============================================================================
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
#==============================================================================

def isprime(x):
    """Returns True if x is a prime a number, else return False"""
    if x == 1:
        return False
    for i in range(2,x):
        if(x%i == 0):
            return False
    return True
        
def gen_primes_list(n):
    """Generates a list of primes numbers up to n"""
    primes = []
    for i in range(2,n+1):
        if(isprime(i)):
            primes.append(i)
    return primes

def biggestprime(x):
    """Finds the biggest prime up to x"""
    while not(isprime(x)):
        x -= 1
    return x

#==============================================================================
# Problem 7:
#     By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
#==============================================================================

def primeofindex(n):
    """Returns the nth prime number"""
    i = 1
    ind = 0
    while ind <= n:
        if isprime(i):
            ind+=1
        i += 1
    if n == 0:
        return 1
    return i-1
    

def prime_factors_slow(x):
    """Finds all the prime factors of X in a very, very, VERY, slow manner"""
    factors = []
    primes = gen_primes_list(x)
    primes.pop(0) #To remove the number 1 from the list
    while x != 1:
        while x%min(primes) != 0:
            primes.pop(0)
        factors.append(min(primes))
        x /= min(primes)
    return factors


def prime_factors(x):
    """Finds all the prime factors and returns a list of them (unsorted)"""
    factors = []
    prime = 2
    while x != 1:
        while x%prime != 0:
            prime += 1
        factors.append(prime)
        x /= prime
    return factors

def max_prime_factor(x):
    """Finds the biggest prime factor of x"""
    prime = 2
    while x != 1:
        while x%prime != 0:
            prime += 1
        x /= prime
    return prime
#==============================================================================
# 
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
#==============================================================================

sieve = [True]*2000000
def mark(sieve, x):
    for i in range(x*x, len(sieve), x):
        sieve[i] = False

    
for x in range(2, int(len(sieve)**0.5)+1):
    if sieve[x]:
        mark(sieve, x)
result = sum([i for i in range(2, len(sieve)) if sieve[i]])

#==============================================================================
# 
#  Input: an integer n > 1.
#  
#  Let A be an array of Boolean values, indexed by integers 2 to n,
#  initially all set to true.
#  
#  for i = 2, 3, 4, ..., not exceeding √n:
#    if A[i] is true:
#      for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
#        A[j] := false.
#  
#  Output: all i such that A[i] is true.
#==============================================================================
