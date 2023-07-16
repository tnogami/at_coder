N = int(input())
A = list(map(int, input().split()))
S = input()

dp = [[0 for _ in range(4)] for _ in range(2**3)]
# dp[n]['101'][2] n文字目まで見て0と2が取ってあってMEまで来ている
dp[0][0] = 0

for n in range(N):
    s = S[n]
    a = A[n]
    if s == 'M':
        dp[1 << a][1] += 1
    elif s == 'E':
        for i in range(2**3):
            if dp[i][1] != 0:
                dp[i | (1 << a)][2] += dp[i][1]
    elif s == 'X':
        for i in range(2**3):
            if dp[i][2] != 0:
                dp[i | (1 << a)][3] += dp[i][2]


ans = 0
for i in range(2**3):
    if i == 1 or i == 5:
        ans += dp[i][3]
    if i == 3:
        ans += 2*dp[i][3]
    if i == 7:
        ans += 3*dp[i][3]

print(ans)
