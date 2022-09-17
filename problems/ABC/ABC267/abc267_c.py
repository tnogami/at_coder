N, M = map(int, input().split())
A = list(map(int,input().split()))

S = sum(A[:M])
tmp = sum([(i+1)*a for i, a in enumerate(A[:M])])
ans = tmp

for i in range(1, N-M+1):
    tmp = tmp - S + M*A[i+M-1]
    S = S - A[i-1] + A[i+M-1]
    ans = max(ans, tmp)

print(ans)

