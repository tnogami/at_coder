import bisect
N, X = map(int, input().split())
L = list(map(int,input().split()))
D = [0]
d = 0
for l in L:
    D.append(d+l)
    d = d+l

idx = bisect.bisect(D, X)
print(idx)