MOD = 998244353 

N = int(input())

dp = [[0]*9 for _ in range(N)]
for i in range(9):
    dp[0][i] = 1

for n in range(N-1):
    for i in range(9):
        if i == 0:
            dp[n+1][i] += dp[n][i]%MOD
            dp[n+1][i+1] += dp[n][i]%MOD
            dp[n+1][i] %= MOD
            dp[n+1][i+1] %= MOD
        elif i == 8:
            dp[n+1][i] += dp[n][i]%MOD
            dp[n+1][i-1] += dp[n][i]%MOD
            dp[n+1][i] %= MOD
            dp[n+1][i-1] %= MOD
        else:
            dp[n+1][i] += dp[n][i]%MOD
            dp[n+1][i-1] += dp[n][i]%MOD
            dp[n+1][i+1] += dp[n][i]%MOD
            dp[n+1][i] %= MOD
            dp[n+1][i-1] %= MOD
            dp[n+1][i+1] %= MOD

print(sum(dp[N-1])%MOD)



# import copy
# MOD = 998244353 

# N = int(input())

# dp = [1]*9

# for n in range(1,N):
#     dp1 = [0]*9
#     for i in range(9):
#         if i == 0:
#             dp1[i] += dp[i]
#             dp1[i+1] += dp[i]
#             # dp[i+1] %= MOD
#             # dp[i+1] %= MOD
#         elif i == 8:
#             dp1[i] += dp[i]
#             dp1[i-1] += dp[i]
#             # dp[i+1] %= MOD
#             # dp[i+1] %= MOD
#         else:
#             dp1[i] += dp[i]
#             dp1[i+1] += dp[i]
#             dp1[i-1] += dp[i]
#             # dp[n+1] %= MOD
#             # dp[n+1] %= MOD
#             # dp[n+1] %= MOD
#     for i in range( 9):
#         dp[i] = (dp1[i])%MOD

# print(sum(dp)%MOD)