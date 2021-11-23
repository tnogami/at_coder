import copy
import bisect
N, K = map(int, input().split())
points = []

for i in range(N):
    n = sum(list(map(int,input().split())))
    points.append(n)

S = copy.copy(points)
S.sort()

for p in points:
    p += 300
    idx = bisect.bisect(S, p)
    r = N-idx+1
    if r <= K:
        print("Yes")
    else:
        print("No")

