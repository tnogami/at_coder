import itertools
MOD = 998244353
N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0]*(3000+2) for j in range(N+1)]

for i in range(a[0], b[0]+1):
    dp[1][i] = 1

for i in range(1,N):
    for j in range(a[i-1], b[i-1]+1):
        if dp[i][j] == 0: continue
        tmp = dp[i][j]%MOD
        dp[i+1][max(j, a[i])] += tmp
        dp[i+1][b[i]+1] -= tmp
    
    dp[i+1] = list(itertools.accumulate(dp[i+1]))

ans = 0
for d in dp[N]:
    d %= MOD
    ans += d
print(ans%MOD)
