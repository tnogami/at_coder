import itertools
from collections import defaultdict

N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]
xtoy = defaultdict(set)
ytox = defaultdict(set)

for p in P:
    x, y = p
    xtoy[x].add(y)
    ytox[y].add(x)

ans = 0

for n1, n2 in itertools.combinations(P, 2):
    x1, y1 = n1
    x2, y2 = n2
    if x1 == x2 or y1 == y2 : continue
    if y2 in xtoy[x1] and x2 in ytox[y1]: ans += 1

print(ans//2)



