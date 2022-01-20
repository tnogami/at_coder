
from heapq import heappush, heappop

N, K = map(int, input().split ())
P = list(map(int,input().split()))

Q = P[:K]
cur = min(Q)
hq = []
for i, p in enumerate(P):
    if i < K-1 :
        heappush(hq, p)
        continue

    if p < cur:
        print(cur)
    else:
        heappush(hq, p)
        cur = heappop(hq)
        print(cur)