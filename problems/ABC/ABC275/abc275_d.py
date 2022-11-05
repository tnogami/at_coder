import sys
sys.setrecursionlimit(10**9)

def dfs(n):
    
    if n in d:
        return d[n]

    ret = dfs(n//2) + dfs(n//3)
    d[n] = ret
    return ret

N = int(input())

d = dict()
d[0] = 1

print(dfs(N))
