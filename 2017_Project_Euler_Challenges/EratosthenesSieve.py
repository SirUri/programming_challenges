sieve = [True]*2000000
def mark(sieve, x):
    for i in range(x*x, len(sieve), x):
        sieve[i] = False

    
for x in range(2, int(len(sieve)**0.5)+1):
    if sieve[x]:
        mark(sieve, x)
result = sum([i for i in range(2, len(sieve)) if sieve[i]])

def gen_primes_list_fast(n):
    """Generates a list of primes up to n using the Sieve of Erastothenes 
    Algorithm"""
    sieve = [True]*(n+1)
    for x in range(2, int(len(sieve)**0.5)+1):
        if sieve[x]:
            mark(sieve, x)
    return [i for i in range(2, len(sieve)) if sieve[i]]

primos = gen_primes_list_fast(100)
teste = []
for j in range(99):
    if not (j%2==0 or j%5==0 or j%7==0 or j%3==0):
        teste.append(j)

for i in range(len(primos)):
    if teste[i] != primos[i]:
        print(teste)