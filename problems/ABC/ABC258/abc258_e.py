
from itertools import accumulate
import bisect

N, Q, X = map(int, input().split())
W = list(map(int,input().split()))
w_sum = sum(W)

WW = W + W
acc = [0]+list(accumulate(WW))

nodes = [[] for _ in range(N)]
cnt = [0] * N

for n in range(N):
    req = X
    ct = 0
    if w_sum < X:
        req = X - (X//w_sum)*w_sum
        ct += (X//w_sum) * N
    
    req += acc[n]
    idx = bisect.bisect_left(acc, req)
    ct += idx - n
    if N <= idx : idx%=N

    nodes[n].append(idx)
    cnt[n] = ct

visited = [False]*N
visited[0] = True
before = [0]
loop = []
cur = 0
while True:
    n = nodes[cur][0]
    if visited[n]:
        flg = False
        for b in before:
            if b == n:
                flg = True
            if flg:
                loop.append(b)
        break
    visited[n] = True
    before.append(n)
    cur = n

l1 = len(before)
l2 = len(loop)
                
for q in range(Q):
    K = int(input())
    K -= 1
    if K < l1:
        print(cnt[before[K]])
    else:
        K -= l1
        print(cnt[loop[K%l2]])
    