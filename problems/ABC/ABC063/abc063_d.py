def bs(n, B, d):
    ct = 0
    for h in H:
        s = max(0, h - B*n)
        ct += -(-s//d)
    return ct <= n

N, A, B = map(int, input().split())
d = A - B
H = [int(input()) for i in range(N)]

ok = 10**10
ng = 0

while 1 < abs(ok-ng):
    mid = (ok+ng)//2
    if bs(mid, B, d):
        ok = mid
    else:
        ng = mid

print(ok)
