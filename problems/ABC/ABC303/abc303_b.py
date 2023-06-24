N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
ans = [[False]*N for _ in range(N)]
ct = N*(N-1)//2

for _A in A:
    for i in range(N-1):
        a = _A[i]-1
        b = _A[i+1]-1
        if ans[a][b] == False: ct -= 1
        ans[a][b] = True
        ans[b][a] = True

print(ct)