import math


def score_calculation(acc_score, k, score):
    if k == 1:
        return score - 1200

    ret = acc_score+(1200/math.sqrt(k-1))
    ret *= 10*(1-(0.9)**(k-1))
    ret *= 0.9
    ret += score
    ret /= 10*(1-(0.9)**(k))
    ret -= (1200/math.sqrt(k))
    return ret


N = int(input())
P = list(map(int, input().split()))

dp = [[-10**12]*(N+1) for _ in range(N+1)]  # N個まで見てK個選んだ時の最高得点

for n in range(N):
    score = P[n]
    for k in range(n+1):
        dp[n+1][k] = max(dp[n+1][k], dp[n][k])
        dp[n+1][k+1] = max(dp[n][k+1],
                           score_calculation(dp[n][k], k+1, score))

print(max(dp[N]))
