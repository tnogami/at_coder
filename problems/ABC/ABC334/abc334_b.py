A, M, L, R = map(int, input().split())
L -= A
R -= A

if L < 0:
    diff = (-L//M + 1) * M
    L += diff
    R += diff

ans = R//M - L//M

if L % M == 0:
    ans += 1

print(ans)