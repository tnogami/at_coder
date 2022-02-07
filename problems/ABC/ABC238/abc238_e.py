import sys
sys.setrecursionlimit(10**9)
def dfs(n):
    visited[n] = True

    for to in nodes[n]:
        if visited[to] : continue
        dfs(to)


N, Q = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for _ in range(Q):
   l, r = map(int, input().split())
   nodes[l-1].append(r)
   nodes[r].append(l-1)

visited = [False]*(N+1)

dfs(0)

if visited[N]:
    print("Yes")
else:
    print("No")


