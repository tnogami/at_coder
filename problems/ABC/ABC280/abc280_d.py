def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def ct_prime(n, m):
    ct = 0
    mul = 1
    while True:
        num = n*mul
        while num % n == 0:
            ct += 1
            num //= n

        if m <= ct:
            break

        mul += 1
    
    return n*mul
 
from collections import Counter
from itertools import count
K = int(input())
primes = prime_factorize(K)
ct = Counter(primes)

ans = 0

for k, v in ct.items():
    ans = max(ans, ct_prime(k, v))

print(ans)
