N, K, X = map(int, input().split())
A = list(map(int,input().split()))

B = []

for a in A:
    if 0 < K:
        k = a//X
        k = min(K, k)
        K -= k
        a -= k*X
        B.append(a)
    else:
        B.append(a)

if 0 < K:
    if len(B) <= K:
        print(0)
    else:
        B.sort()
        print(sum(B[:-K]))
else:
    print(sum(B))



