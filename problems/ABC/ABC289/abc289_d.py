N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
X = int(input())

dp = [False]*(10**5+10)

dp[0] = True

for b in B:
    dp[b] = -1


for k in range(10**5+1):
    if not dp[k] or dp[k] == -1 : continue

    for a in A:
        to = k + a
        if 10**5+5 < to: continue
        if dp[to] == -1: continue
        dp[to] = True

if dp[X]:
    print("Yes")
else:
    print("No")
