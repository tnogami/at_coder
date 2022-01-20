import sys
sys.setrecursionlimit(10**9)
def dfs(n, nodes):
    seen[n] = True
    visited.append(n)

    for to in nodes[n]:
        if seen[to] : continue
        dfs(to, nodes)
    memo.append(n)

N, M = map(int, input().split())
nodes = [set() for i in range(N)]
nodes_rev = [set() for i in range(N)]
visited = []
memo = []

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a-1].add(b-1)
    nodes_rev[b-1].add(a-1)

#行き掛けの番号を記録
seen = [False for i in range(N)]
for i in range(N):
    if seen[i] : continue
    dfs(i, nodes)
memo.reverse()

seen = [False for i in range(N)]
ans = 0
for i in memo[:]:
    if seen[i] : continue
    visited = []
    dfs(i, nodes_rev)

    k = len(visited)
    ans += k*(k-1)//2

print(ans)