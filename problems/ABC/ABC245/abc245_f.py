# from collections import deque

# N, M = map(int, input().split())
# nodes = [[set(), set()] for _ in range(N)]

# for _ in range(M):
#     u, v = map(int, input().split())
#     nodes[u-1][0].add(v-1)
#     nodes[v-1][1].add(u-1)

# # que = deque([i for i in range(N) if len(nodes[i][0]) == 0])
# ans = [True]*N
# while que:
#     i = que.popleft()
#     ans[i] = False
#     for frm in nodes[i][1]:
#         if i in nodes[frm][0]:
#             nodes[frm][0].remove(i)
#             if len(nodes[frm][0]) == 0:
#                 que.append(frm)

# print(ans.count(True))

#別解
# 強連結成分分解
from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    seen1[i] = True
    for to in G[i]:
        if seen1[to]:
            continue
        dfs(to)
    visited_order.append(i)

def r_dfs(i):
    seen2[i] = True
    s.append(i)
    for to in RG[i]:
        if seen2[to]:
            continue
        r_dfs(to)

N, M = map(int, input().split())
G = defaultdict(list)
RG = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    RG[v-1].append(u-1)

visited_order = []
groups = []

seen1 = [False]*N
for i in range(N):
    if seen1[i]:
        continue
    dfs(i)

seen2 = [False]*N
for i in visited_order[::-1]:
    if seen2[i]: continue
    s = []
    r_dfs(i)
    groups.append(s)

K = len(groups)
ans = 0

seen = [False]*N
que = deque()
for v in groups:
    if len(v) == 1:
        continue
    for i in v:
        seen[i] = True
    que.extend(v)

while que:
    cur = que.popleft()
    for to in RG[cur]:
        if seen[to]:continue
        que.append(to)
        seen[to] = True

print(seen.count(True))