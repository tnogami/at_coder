from collections import Counter
#因数分解
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


N = int(input())
A = prime_factorize(N)
ct = Counter(A)
ans = 0
for i in ct.values():
    tmp = 0
    for k in range(10000):
        tmp += k+1
        if i < tmp+k+2:
            ans += k+1
            break

print(ans)



