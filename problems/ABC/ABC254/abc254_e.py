def dfs(n,m):
    global ans

    ans.add(n+1)

    if m == k:return

    for to in nodes[n]:
        if to in visited:continue
        visited.add(to)
        dfs(to,m+1)
        visited.remove(to)

N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    visited = set()
    ans = set()
    dfs(x-1,0)
    print(sum(ans))