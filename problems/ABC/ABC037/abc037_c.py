N, K = map(int, input().split())
A = list(map(int,input().split()))

ans = sum(A[:K])
s = ans
for i in range(N-K):
    s -= A[i]
    s += A[i+K]
    ans += s

print(ans)
