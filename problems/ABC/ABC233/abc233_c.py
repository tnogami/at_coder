def dfs(idx, prdct):
    if idx == N:
        ans.append(prdct)
        return

    for a in A[idx]:
        dfs(idx+1, prdct*a)

N, X = map(int, input().split())
L = []
A =[[] for i in range(N)]
ans = []


for i in range(N):
    inp = list(map(int, input().split()))
    L.append(inp[1])
    for j in inp[1:]:
        A[i].append(j)

dfs(0, 1)
print(ans.count(X))



