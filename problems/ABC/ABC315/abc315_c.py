from heapq import heappush, heappop
N = int(input())
d = dict()

for n in range(N):
    f, s = map(int, input().split())
    if f in d:
        heappush(d[f], -s)
    else:
        d[f] = [-s]

m1, m2 = 0, 0
tmp = []
m3 = 0
for s in d.values():
    heappush(tmp, min(s))
    if 1 < len(s):
        a = -heappop(s)
        b = -heappop(s)
        m3 = max(m3, a+b//2)

if 1 < len(tmp):
    a = -heappop(tmp)
    b = -heappop(tmp)
    ans = max(a+b, m3)
else:
    ans = m3

print(ans)
