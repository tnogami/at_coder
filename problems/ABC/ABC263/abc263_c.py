from itertools import combinations
N, M = map(int, input().split())

ans = []
for comb in combinations(range(1,M+1), N):
    tmp = list(comb)
    tmp.sort()
    ans.append(tmp)

for a in ans:
    print(*a)