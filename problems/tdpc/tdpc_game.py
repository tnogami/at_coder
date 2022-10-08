import itertools

N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_acc = [0]+list(itertools.accumulate(A[::-1]))
B_acc = [0]+list(itertools.accumulate(B[::-1]))
dp = [[0]*(N+1) for _ in range(M+1)]

for a in range(N):
    for b in range(M):
        # aを取る
        dp[b][a+1] = max(dp[b][a+1], A[-(a+1)] + B_acc[b] + A_acc[a] - dp[b][a])
        # bを取る
        dp[b+1][a] = max(dp[b+1][a], B[-(b+1)] + B_acc[b] + A_acc[a] - dp[b][a])
print(dp)
print(dp[M][N])




