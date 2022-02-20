import sys
sys.setrecursionlimit(10**9)
def dfs(n):
    visited[n] = True

    ret = 1
    for to in nodes[n]:
        if visited[to] : continue
        ret += dfs(to)
    dp[n] = (N-ret)*ret
    return ret


N = int(input())
nodes = [[] for _ in range(N)]

for _ in range(N-1):
   a, b = map(int, input().split())
   nodes[a-1].append(b-1)
   nodes[b-1].append(a-1)

visited = [False]*N
dp = [0]*N
dfs(0)
print(sum(dp))