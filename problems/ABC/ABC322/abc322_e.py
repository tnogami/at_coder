from itertools import product
N, K, P = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

states = [int(''.join(list(map(str, comb))))
          for comb in product(range(P+1), repeat=K)]
dp = [{state: 10**18 for state in states} for _ in range(N+1)]

for i in range(N):
    c = A[i][0]
    scores = A[i][1:]

    for comb in product(range(P+1), repeat=K):
        from_state = int(''.join(list(map(str, comb))))

        to_state = [min(P, comb[k]+scores[k]) for k in range(len(scores))]
        to_state = int(''.join(list(map(str, to_state))))

        # 取らない場合
        dp[i+1][from_state] = min(dp[i+1][from_state], dp[i][from_state])

        # 取る場合
        if from_state == 0:
            dp[i+1][to_state] = min(dp[i+1][to_state], c)
        else:
            dp[i+1][to_state] = min(dp[i+1][to_state], dp[i][from_state] + c)

if dp[N][int(str(P)*K)] == 10**18:
    print(-1)
else:
    print(dp[N][int(str(P)*K)])
