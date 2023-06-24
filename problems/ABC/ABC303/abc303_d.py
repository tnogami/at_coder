X, Y, Z = map(int, input().split())

S = input()

dp = [[10**18]*2 for _ in range(len(S)+1)]
dp[0][0] = 0

if len(S) == 1:
    if S == 'A':
        print(min(Y, Z+X))
    else:
        print(X)
else:
    for i, s in enumerate(S):

        if s == 'A':
            dp[i+1][0] = min(dp[i+1][0], dp[i][0]+Y, dp[i][1]+X+Z, dp[i][1]+Z+Y)
            dp[i+1][1] = min(dp[i+1][1], dp[i][0]+Z+X, dp[i][0]+Y+Z, dp[i][1]+X)
        else:
            dp[i+1][0] = min(dp[i+1][0], dp[i][0]+X, dp[i][1]+Z+X, dp[i][1]+Y+Z)
            dp[i+1][1] = min(dp[i+1][1], dp[i][0]+X+Z, dp[i][0]+Z+Y, dp[i][1]+Y)
    
    print(min(dp[len(S)]))