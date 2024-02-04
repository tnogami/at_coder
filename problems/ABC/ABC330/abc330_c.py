D = int(input())

ans = 10**21
for x in range(2*10**6+3):
    if x**2 >= D:
        ans = min(ans, x**2-D)
        continue

    ok = 2*10**6+3
    ng = 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if mid**2 >= D-x**2:
            ok = mid
        else:
            ng = mid
    ans = min(ans, x**2+ok**2-D)

for x in range(2*10**6+3):
    if x**2 >= D:
        continue

    ng = 2*10**6+3
    ok = 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if mid**2 > D-x**2:
            ng = mid
        else:
            ok = mid
    ans = min(ans, -(x**2+ok**2-D))

print(ans)
