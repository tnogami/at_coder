
import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    order.append(i+1)

    if i == Y-1:
        print(*order)
    
    for j in nodes[i]:
        if visited[j] == True : continue
        dfs(j)

    order.pop()

N, X, Y = map(int, input().split())

nodes = [[] for _ in range(N)]
visited = [False] * N
order = []

for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].append(v)
    nodes[v].append(u)

dfs(X-1)

print(*order)
