from collections import defaultdict
from itertools import permutations


N, C = map(int, input().split())

D = [list(map(int, input().split())) for _ in range(C)]
colors = [list(map(int, input().split())) for _ in range(N)]

groups = [defaultdict(int) for _ in range(3)]

ans = 10**19
for i in range(N):
    for j in range(N):
        c = colors[i][j]
        k = (i+j)%3
        groups[k][c-1] += 1

for p in permutations(range(C), 3):
    tmp = 0
    for i, c_after in enumerate(p):
        for c_before, num in groups[i].items():
            tmp += num*D[c_before][c_after]
    ans = min(tmp, ans)

print(ans)

