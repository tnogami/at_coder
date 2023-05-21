N, M, D = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()

idx_a = N-1
idx_b = M-1

ans = -1
while True:

    if abs(A[idx_a]-B[idx_b]) <= D:
        ans = max(ans, A[idx_a]+B[idx_b])
        break

    if A[idx_a]>B[idx_b]:
        idx_a -= 1
        if idx_a == -1:
            break
    else:
        idx_b -= 1
        if idx_b == -1:
            break

print(ans)