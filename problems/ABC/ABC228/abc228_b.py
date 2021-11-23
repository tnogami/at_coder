N, X = map(int, input().split())
A = list(map(int,input().split()))

ans = [False for i in range(N)]

i = X-1
while not ans[i]:
    ans[i] = True
    i = A[i] - 1

print(ans.count(True))
