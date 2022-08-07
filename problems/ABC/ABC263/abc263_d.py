N, L, R = map(int, input().split())
A = list(map(int,input().split()))
S = sum(A)
X = [0]*N
Y = [0]*N

t = 0
best = 0
for i, a in enumerate(A):
    t += L - a
    best = min(best, t)
    X[i] = best

t = 0
best = 0
for i in range(N-1, -1, -1):
    a = A[i]
    t += R - a
    best = min(best, t)
    Y[i] = best

X = [0] + X + [0]
Y = [0] + Y + [0]

ans = 10**21
for i in range(N+1):
    ans = min(ans, X[i]+Y[i+1])

print(S+ans)
