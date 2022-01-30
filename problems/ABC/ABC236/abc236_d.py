import copy

def dfs(n, a, s):
    global ans 
    if n == 2*N - 1:
        ans = max(ans, a)
        return
    if n in s:
        dfs(n+1, a, s)
    else:
        for i, b in enumerate(A[n]):
            if i+1+n in s: continue
            new_a = a^b
            new_s = copy.copy(s)
            new_s.add(i+1+n)
            new_s.add(n)
            dfs(n+1, new_a, new_s)


N = int(input())
A = [list(map(int, input().split())) for _ in range(2*N-1)]

ans = -1
s = set()
dfs(0, 0, s)

print(ans)