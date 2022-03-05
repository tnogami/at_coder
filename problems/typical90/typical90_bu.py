MOD = (10**9) + 7


def dfs(n):

    visited[n] = True
    is_leaf = True

    dp[n][color[n]] = 1
    for to in nodes[n]:
        if visited[to]: continue
        dfs(to)
        one = dp[n][color[n]]*dp[to][color[n]]%MOD + dp[n][color[n]]*dp[to][2]%MOD
        both = dp[n][2]*(dp[to][0]+dp[to][1]+2*dp[to][2])%MOD + dp[n][color[n]]*(dp[to][(color[n]+1)%2]+dp[to][2])%MOD
        dp[n][color[n]] = one%MOD
        dp[n][2] = both%MOD

N = int(input())
color = list(map(lambda x : 0 if x == "a" else 1 , input().split()))
nodes = [[] for _ in range(N)]
for _ in range(N-1):
   a, b = map(int, input().split())
   nodes[a-1].append(b-1)
   nodes[b-1].append(a-1)

dp = [[0]*3 for _ in range(N)]
visited = [False] * N

dfs(0)
print(dp[0][2])

