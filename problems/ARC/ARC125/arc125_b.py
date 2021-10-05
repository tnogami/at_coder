import math
N = int(input())
ans = 0
for q in range(1, int(math.sqrt(N))+1):
    limit = N//q - q
    ans += limit//2 + 1
    ans %= 998244353
print(ans)
