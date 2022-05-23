import sys
sys.setrecursionlimit(10**9)
def dfs(n, dist):

    for to in nodes[n]:
        if dist[to] != -1:
            continue

        dist[to] = dist[n] + 1
        dfs(to,dist)

N, u, v = map(int, input().split())
nodes = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

dist_t = [-1]*N
dist_a = [-1]*N

dist_t[u-1] = 0
dist_a[v-1] = 0

dfs(u-1, dist_t)
dfs(v-1, dist_a)

ans = 0
for i in range(N):
    if dist_t[i] < dist_a[i]:
        tmp = dist_a[i] - 1
        ans = max(tmp, ans)

print(ans)