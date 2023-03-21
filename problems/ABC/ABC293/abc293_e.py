def dfs(x):
    if x == 1:
        return 1
    
    if x%2 == 0:
        return (dfs(x//2) * (pow(A,x//2,M) + 1))%M
    else:
        return (A * dfs(x//2) * (pow(A, x//2, M) + 1) + 1)%M

A, X, M = map(int, input().split())

print(dfs(X)%M)