from collections import defaultdict
d = defaultdict(int)


N, Q = map(int, input().split())
A = [i for i in range(N)]

for i in range(N):
    d[i] = i

for _ in range(Q):
    x = int(input())
    x -= 1
    pos = d[x]
    if pos == N-1:
        A[N-2], A[N-1] = A[N-1], A[N-2]
        d[x] -= 1
        d[A[N-1]] += 1
    else:
        A[pos], A[pos+1] = A[pos+1], A[pos]
        d[x] += 1
        d[A[pos]] -= 1

A = list(map(lambda x:x+1, A))
print(*A)
        




