
import sys
sys.setrecursionlimit(10**9)
mod = 998244353
memo = dict()

def dfs(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    if n in memo:
        return memo[n]

    ret = 0
    for m in range(2, 7):
        if n%m != 0 : continue
        ret += pow(5, mod-2, mod)*dfs(n//m)
        ret %= mod

    memo[n] = ret

    return ret

N = int(input())

print(dfs(N))