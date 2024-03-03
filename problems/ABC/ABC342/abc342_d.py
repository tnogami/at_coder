from collections import Counter
zero_ct = 0
def prime_factorize(n):
    global zero_ct
    if n == 1:
        return []
    if n == 0:
        zero_ct += 1
        return -1
    a = Counter()
    while n % 2 == 0:
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] += 1

    ret = []
    for k, v in a.items():
        if v % 2 == 1:
            ret.append(k)

    return sorted(ret)

N = int(input())
A = list(map(int,input().split()))
B = [prime_factorize(a) for a in A]

d = dict()

ans = 0

for a in B:
    if a == -1:
        continue
    if not a:
        if 'ok' in d:
            ans += d['ok']
            d['ok'] += 1
        else:
            d['ok'] = 1
    else:
        if tuple(a) in d:
            ans += d[tuple(a)]
            d[tuple(a)] += 1
        else:
            d[tuple(a)] = 1

ans += zero_ct * (N - zero_ct) + zero_ct * (zero_ct - 1) // 2

print(ans)



