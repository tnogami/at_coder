N = int(input())
K = int(input())
L = len(str(N))
dp = [[[0]*(K+1) for i in range(2)] for i in range(L+1)]
dp[0][0][0] = 1

for i in range(N):
    for smaller in range(2):
        for k in range(K+1):
            for x in range(9):
                if smaller == 0:
                    dp[i+1][smaller][k] += dp[i][smaller][k]
                    
                else:
                dp[i+1][smaller][k] += dp[i][smaller][k]
            

