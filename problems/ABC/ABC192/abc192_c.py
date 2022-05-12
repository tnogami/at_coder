N, K = map(int, input().split())
before = -1
for i in range(K):
    
    g1 = [i for i in str(N)]
    g2 = [i for i in str(N)]
    g1.sort(reverse=True)
    g2.sort(reverse=False)
    g1 = int("".join(g1))
    g2 = int("".join(g2))
    N = g1 - g2

    if N == before:
        break
    else:
        before = N

print(N)