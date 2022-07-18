import sys
sys.setrecursionlimit(10**9)

def dfs(color, rev, num):
    global ct
    if rev == 1 and color == 1:
        ct += num
        return

    if rev == 1 and color == 0: return

    if color == 0:
        dfs(0, rev-1, num)
        dfs(1, rev, num*X)
    else:
        dfs(0, rev-1, num)
        dfs(1, rev-1, num*Y)

N, X, Y = map(int, input().split())

ct = 0

dfs(0, N, 1)

print(ct)
