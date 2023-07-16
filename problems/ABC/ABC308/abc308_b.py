N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

prices = dict()
for d, p in zip(D, P[1:]):
    prices[d] = p

ans = 0
for c in C:
    if c in prices:
        ans += prices[c]
    else:
        ans += P[0]

print(ans)
