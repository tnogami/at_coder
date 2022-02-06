MOD = 998244353
N = int(input())
digit = len(str(N))
ans = 0
for i in range(1, N):
    ans += ((1+int("9"+"0"*(i-1)))*9*10**(i-1))//2
    ans %= MOD

m = 10**(digit-1)
n = N - m + 1
M = (n+1)*n//2
M %= MOD

ans += M

print(ans%MOD)