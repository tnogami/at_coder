import sys
sys.setrecursionlimit(10**9)

def dfs(n, d):
    s = 1
    dist[n] = d
    for to in nodes[n]:
        if dist[to] != -1 : continue
        s += dfs(to, d+1)

    size[n] = s
    return s

def dfs_ans(n, a):
    visited[n] = True
    ans[n] = a
    for to in nodes[n]:
        if visited[to] == True : continue
        dfs_ans(to, a-2*size[to]+N)
    return

N = int(input())
nodes = [[] for i in range(N)]
dist = [-1]*N
size = [0]*N

for i in range(N-1):
    u, v = map(int, input().split())
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)

dfs(0,0)
dist_org = sum(dist)

ans = [0]*N
visited = [False]*N

dfs_ans(0, dist_org)

for a in ans:
    print(a)