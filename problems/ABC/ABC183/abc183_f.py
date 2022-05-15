from collections import defaultdict
N, Q = map(int, input().split())
C = list(map(int,input().split()))

dicts = [defaultdict(int) for _ in range(N)]
for i in range(N):
    dicts[i][C[i]-1] = 1

group = list(range(N))
members = [[i] for i in range(N)]

for _ in range(Q):
    q, ax, by = map(int, input().split())
    ax -= 1
    by -= 1
    if q == 1:
        if group[ax] == group[by]: continue
        if len(members[group[ax]]) < len(members[group[by]]):
            pass
        else:
            ax, by = by, ax
        for i in members[group[ax]]:
            members[group[by]].append(i)
            group[i] = group[by]
            dicts[group[by]][C[i]-1] += 1
    else:
        print(dicts[group[ax]][by])