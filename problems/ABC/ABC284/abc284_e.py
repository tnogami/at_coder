import sys
sys.setrecursionlimit(10**9)

def dfs(n):

    global ans

    if ans == 10**6:
        print(10**6)
        exit()

    for to in nodes[n]:
        if visited[to]: continue
        visited[to] = True
        ans += 1
        dfs(to)
        visited[to] = False

    return

N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)


visited = [False]*N
visited[0] = True
ans = 1
dfs(0)
print(ans)
