
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

N = int(input())
primes = f_primes(10**6+10)

ans = 0
for i in range(len(primes)):
    a = primes[i]
    if N < a**3:break
    for j in range(i+1, len(primes)):
        b = primes[j]
        c = primes[j+1]
        if N < a**2*b*c**2: break
        
        ok = j+1
        ng = len(primes)-1

        while 1 < abs(ok-ng):
            mid = (ok+ng)//2

            if N < a**2*b*primes[mid]**2:
                ng = mid
            else:
                ok = mid

        ans += ok - j

print(ans)        