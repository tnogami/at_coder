
# def cal_nex(S):
#     ret = [[N]*26 for i in range(N+1)]

#     for i in range(N-1, -1, -1):
#         for j in range(26):
#             ret[i][j] = ret[i+1][j]
        
#         idx = ord(S[i]) - ord("a")
#         ret[i][idx] = i

#     return ret

N, K = map(int, input().split())
S = input()

dp = [[[] for _ in range(26)] for _ in range(N+1)]

for n in range(N):
    for i in range(26):
        # dp[n+1][i] = [c for c in dp[n][i]]
        dp[n+1][i] = dp[n][i]
        if ord(S[n])-ord("a") <= i:
            dp[n+1][i].append(S[n])

ans = []
for d in dp[-1]:
    if K <= len(d):
        ans.append("".join(d[:K]))

ans.sort()
print(ans)
print(ans[0])








