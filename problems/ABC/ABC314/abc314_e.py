from collections import Counter


N, M = map(int, input().split())
C = []
P = []
S = []
ct = []
for n in range(N):
    cps = list(map(int, input().split()))
    C.append(cps[0])
    P.append(cps[1])
    S.append(sorted(list(set(cps[2:]))))
    ct.append(Counter(cps[2:]))

dp = [0]*(M+1)

for m in range(M-1, -1, -1):
    tmp = 10000000
    for n in range(N):  # どのスロットを選ぶか
        score = 0
        flag = False
        for i, s in enumerate(S[n]):  # どの目がでるか
            if M <= m + s:
                score += C[n]*ct[n][s]/P[n]
            elif s == 0:
                flag = True
                score += C[n]*ct[n][s]/P[n]
                t = 1/(1-ct[n][s]/P[n])
            else:
                score += (dp[m+s]+C[n])*ct[n][s]/P[n]
        if flag:
            score *= t
        tmp = min(tmp, score)
    dp[m] = tmp

print(dp[0])
