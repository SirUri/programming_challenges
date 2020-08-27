#==============================================================================
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
#==============================================================================

def isprime(x):
    """Returns True if x is a prime a number, else return False"""
    if x == 1:
        return True
    for i in range(2,x):
        if(x%i == 0):
            return False
    return True
        
def gen_primes_list(n):
    """Generates a list of primes numbers up to n"""
    primes = []
    for i in range(1,n+1):
        if(isprime(i)):
            primes.append(i)
    return primes

def biggestprime(x):
    """Finds the biggest prime up to x"""
    while not(isprime(x)):
        x -= 1
    return x


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


            
    