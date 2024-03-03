d = dict()
d[1] = 0
d[2] = 2
d[3] = 5

def dfs(n):
    if n in d:
        return d[n]

    d[n] = dfs(n//2) + dfs(-(-n//2)) + n
    
    return d[n]

N = int(input())
ans = dfs(N)

print(ans)