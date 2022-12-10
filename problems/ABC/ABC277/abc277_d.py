
N, K = map(int, input().split())
A = list(map(int,input().split()))
A.sort()

M = sum(A)

A = A+A

minus = 0
cur = -1

ans = 10**21

for i in range(2*N):
    if cur == -1:
        cur = A[i]
        minus += A[i]
        continue

    if cur == A[i]:
        minus += A[i]
        continue

    if (cur+1)%K == A[i]:
        cur = (cur+1)%K
        minus += A[i]
        continue

    ans = min(ans, M-minus)
    cur = A[i]
    minus = A[i]

ans = min(ans, M-minus)


print(max(0, ans))
