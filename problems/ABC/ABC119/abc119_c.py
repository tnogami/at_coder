from itertools import product
N, A, B, C = map(int, input().split())
L = [int(input()) for l in range(N)]

ans = 10**10
for k in product(range(4), repeat=N):
    if 0 not in k or 1 not in k or 2 not in k: continue

    a = []
    b = []
    c = []
    for i, d in enumerate(k):
        if d == 0:
            a.append(L[i])
        elif d == 1:
            b.append(L[i])
        elif d == 2:
            c.append(L[i])
    
    tmp = (len(a)-1)*10
    a = sum(a)
    tmp += abs(a-A)

    tmp += (len(b)-1)*10
    b = sum(b)
    tmp += abs(b-B)

    tmp += (len(c)-1)*10
    c = sum(c)
    tmp += abs(c-C)

    ans = min(ans, tmp)

print(ans)












