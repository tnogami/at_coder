N = int(input())

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

primes = f_primes(10**6)
ans = 0
for i, p in enumerate(primes):
    ok = 0
    ng = len(primes)-1
    while 1 < abs(ok-ng):
        m = (ok+ng)//2
        if p*primes[m]**3 <= N:
            ok = m
        else:
            ng = m
    
    if ok <= i:break

    ans += ok-i

print(ans)
