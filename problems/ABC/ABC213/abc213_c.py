import bisect
H, W, N = map(int, input().split())
HA = set([])
WB = set([])
AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append((A,B))
    HA.add(A)
    WB.add(B)

HA = list(HA)
WB = list(WB)
HA.sort()
WB.sort()

for a,b in AB:
    h = bisect.bisect_left(HA, a) + 1
    w = bisect.bisect_left(WB, b) + 1
    print(h,w)