import sys
sys.setrecursionlimit(10**9)

def dfs(n):
    if n == 1:
        return [1]
    tmp = dfs(n-1)
    ret = tmp + [n] + tmp
    return ret

N = int(input())
L = 1
print(*dfs(N))
