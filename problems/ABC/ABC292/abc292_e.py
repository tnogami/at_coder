import sys
sys.setrecursionlimit(10**9)

def dfs(n):
    visited[n] = True
    for to in nodes[n]:
        if visited[to] :continue
        dfs(to)

N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
edges = set()
for _ in range(M):
    u, v = map(int, input().split())
    nodes[u-1].append(v-1)
    edges.add((u)**131+(v)*1007)

ans = 0

for n in range(N):
    visited = [False]*N
    dfs(n)
    for i, v in enumerate(visited):
        if i == n: continue
        if v: edges.add((n+1)**131+(i+1)*1007)

print(len(edges)-M)