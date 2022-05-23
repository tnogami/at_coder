def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

from collections import defaultdict

N, K = map(int, input().split())
S = list(input())

M = make_divisors(N)[::-1]

for m in M:
    ans = N//m
    d = [defaultdict(int) for _ in range(ans)]
    for i, s in enumerate(S):
        d[i%ans][s] += 1
    
    reqK = 0
    for k in d:
        reqK += m - max(k.values())
    
    if reqK <= K:
        break

print(ans)

