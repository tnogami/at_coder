
def dfs(node, cost):
    global ans

    if all([visited[i] for i, c in nodes[node]]):
        ans = max(ans, cost)
        return

    for i, c in nodes[node]:
        if not visited[i]:
            visited[i] = True
            cost += c
            dfs(i, cost)
            cost -= c
            visited[i] = False


N, M = map(int, input().split())
nodes = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    nodes[a-1].append((b-1, c))
    nodes[b-1].append((a-1, c))

visited = [False]*N

ans = 0
for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(ans)
