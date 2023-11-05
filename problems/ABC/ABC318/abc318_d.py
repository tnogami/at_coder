import sys
sys.recursionlimit = 10**8


def dfs(n, i):
    global ans
    ans = max(ans, n)
    if i == N-1:
        return
    if paired[i]:
        dfs(n, i+1)
    else:
        for k, d in enumerate(D[i]):
            if not paired[k+i+1]:
                paired[k+i+1] = True
                dfs(n+d, i+1)
                paired[k+i+1] = False


N = int(input())
D = [list(map(int, input().split())) for _ in range(N-1)]

if N % 2 == 1:
    D = [[0]*N] + D
    N += 1

ans = 0
paired = [False]*N

dfs(0, 0)

print(ans)
