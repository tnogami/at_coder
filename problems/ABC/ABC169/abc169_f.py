import sys
from itertools import accumulate

sys.setrecursionlimit(10**9)

MOD = 998244353

def dfs(i,s,ct):
    global groups

    if s == S:
        groups.append(ct)
        return
    
    if i == N:
        return

    if restAsum[i] < S - s :
        return

    for k in range(2):
        if k == 0:
            dfs(i+1, s+A[i], ct+1)
        else:
            dfs(i+1, s, ct)

N, S = map(int, input().split())
A = list(map(int,input().split()))

restAsum = list(accumulate(A[::-1]))
restAsum = restAsum[::-1]

groups = []

dfs(0,0,0)

ans = 0
for k in groups:
    ans += pow(2, N-k, MOD)
    ans %= MOD

print(ans)
