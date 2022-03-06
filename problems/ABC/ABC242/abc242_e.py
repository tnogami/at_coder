import copy
MOD = 998244353
def tw6th(s):
    ret = 0
    x = 1
    for i, c in enumerate(s[::-1]):
        ret += (ord(c)-ord("A"))*x
        x *= 26
        ret %= MOD
        x %= MOD
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    n = -(-N//2)
    ans = tw6th(S[:n])

    if N%2 == 0:
        if S[:n]+S[:n][::-1] <= S : ans += 1
    else:
        if S[:n]+S[:n-1][::-1] <= S : ans += 1
    print(ans%MOD)

