N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)

average = P / D
ct = 0
for f in F:
    if f > average:
        ct += 1

ct_buy = ct // D

ans = 10**18
tmp = ct_buy * P
for i, f in enumerate(F):
    if i < ct_buy*D:
        tmp += 0
    else:
        tmp += f

ans = min(ans, tmp)

ct_buy += 1
tmp = ct_buy * P
for i, f in enumerate(F):
    if i < ct_buy*D:
        tmp += 0
    else:
        tmp += f

ans = min(ans, tmp)
print(ans)
