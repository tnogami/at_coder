# 強連結成分分解
from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

def SCC(N, G, rG):
    group_num = 0
    visited_order = []
    group = defaultdict(int)
    groups = []
   
    def dfs(i):
        seen[i] = True
        for to in G[i]:
            if seen[to] : continue
            dfs(to)
        visited_order.append(i)

    def r_dfs(i):
        seen[i] = True
        s.append(i)
        group[i] = group_num
        for to in rG[i]:
            if seen[to] : continue
            r_dfs(to)

    seen = [False]*N
    for i in range(N):
        if not seen[i]:
            dfs(i)

    seen = [False]*N
    for i in visited_order[::-1]:
        if not seen[i]:
            s = []
            r_dfs(i)
            groups.append(s)
            group_num += 1

    ret_G = [set([]) for _ in range(group_num)]
    for i in range(N):
        frm = group[i]
        for to in G[i]:
            if frm == group[to] : continue
            ret_G[frm].add(group[to])

    return groups, ret_G

N = int(input())
X = list(map(int,input().split()))
C = list(map(int,input().split()))
G = [[] for _ in range(N)]
rG = [[] for _ in range(N)]

for i, x in enumerate(X):
    G[i].append(x-1)
    rG[x-1].append(i)

groups, graph = SCC(N,G,rG)

ans = 0
for g in groups:
    if len(g) == 1:continue
    tmp = []
    for n in g:
        tmp.append(C[n])

    ans += min(tmp)

print(ans)


