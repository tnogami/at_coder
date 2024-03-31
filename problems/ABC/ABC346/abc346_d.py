N = int(input())
S = list(input())
costs = list(map(int,input().split()))

cost_10 = []
tmp = 0
for i, s in enumerate(S):
    if int(s) != (i+1)%2:
        tmp += costs[i]
    cost_10.append(tmp)

cost_01 = []
tmp = 0
for i, s in enumerate(S):
    if int(s) != i%2:
        tmp += costs[i]
    cost_01.append(tmp)

ans = 10**21
for i in range(N-1):
    # S[i]とS[i+1]が同じ数字
    ans = min(ans, cost_10[i]+cost_01[N-1]-cost_01[i])
    ans = min(ans, cost_01[i]+cost_10[N-1]-cost_10[i])

print(ans)