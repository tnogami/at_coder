MOD = 998244353

N, A, B, P, Q = map(int, input().split())

dp_t = [[0]*(N+1) for _ in range(N+1)]
dp_a = [[0]*(N+1) for _ in range(N+1)]

dp_t[0][A] = 1
dp_a[0][B] = 1

for n in range(N):
    for i in range(A, N):
        for k in range(1, P+1):
            dp_t[n+1][min(i+k, N)] += pow(P, MOD-2, MOD)*dp_t[n][i]
            dp_t[n+1][min(i+k, N)] %= MOD

for n in range(N):
    for i in range(B, N):
        for k in range(1, Q+1):
            dp_a[n+1][min(i+k, N)] += pow(Q, MOD-2, MOD)*dp_a[n][i]
            dp_a[n+1][min(i+k, N)] %= MOD
            
ans = 0


for i in range(N+1):
    base = dp_t[i][N]
    for j in range(i, N+1):
        ans += base*dp_a[j][N]
        ans %= MOD
print(ans)
            

