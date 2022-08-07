MOD = 998244353
N = int(input())
A = list(map(int,input().split()))

acc = [0, 0]
for i in range(N-2, -1, -1):
    a = A[i]
    ak = (acc[-1]-acc[-a-1]+a+1) * pow(a, MOD-2, MOD)
    ak %= MOD
    acc.append(acc[-1]+ak)

ans = (acc[-1]-acc[-2])%MOD
print(ans%MOD)