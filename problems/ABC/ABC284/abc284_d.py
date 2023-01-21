import math

#素数列挙
def f_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

T = int(input())
Ts = [int(input()) for _ in range(T)]
Tmax = max(Ts)
primes = f_primes(10**7)

for t in Ts:
    for prime in primes:
        if t%prime == 0:
            if t%prime**2 == 0:
                p = prime
                q = t//prime**2
            else:
                q = prime
                p = int(math.sqrt(t//q))
            break

    print(p, q)


        

