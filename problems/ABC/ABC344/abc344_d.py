T = input()
N = int(input())
A = []

for _ in range(N):
    l = input().split()
    A.append(l[1:])

dp = [[10**18]*(len(T) + 1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0
for i in range(len(A)):
    a = A[i]
    for t in range(len(T)+1):
        if dp[i][t] == 10**18:
            continue

        dp[i+1][t] = min(dp[i+1][t], dp[i][t])

        for s in a:
            if t + len(s) <= len(T) and T[t:t+len(s)] == s:
                dp[i+1][t+len(s)] = min(dp[i+1][t+len(s)], dp[i][t] + 1)


print(dp[-1][-1]) if dp[-1][-1] != 10**18 else print(-1)
