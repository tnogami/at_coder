import bisect
def dfs(s, d):
    if len(s) == N:
        ans.append(int(s))
        return
    
    for i in range(0,10):
        if i - int(s[-1]) == d:
            next_s = s+str(i)
            dfs(next_s, d)

X = int(input())

N = len(str(X))

ans = []

for d in range(-9,9):
    for i in range(1,10):
        dfs(str(i), d)

print(ans)
ans.sort()
idx = bisect.bisect_left(ans, X)
print(ans[idx])