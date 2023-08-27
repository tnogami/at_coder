H, W, N = map(int, input().split())
holes = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(N)]
s_holes = set(holes)

acc = [[0]*W for _ in range(H)]
for hole in holes:
    h, w = hole
    acc[h][w] = 1

for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            continue
        elif h == 0:
            acc[h][w] += acc[h][w-1]
        elif w == 0:
            acc[h][w] += acc[h-1][w]
        else:
            acc[h][w] += acc[h-1][w] + acc[h][w-1] - acc[h-1][w-1]


def my_bisect(h, w):
    ok = 0
    ng = min(H-h-1, W-w-1)

    if ok == ng:
        return ok

    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if acc[h+ok][w+ok] == acc[h+mid][w+mid]:
            ok = mid
        else:
            ng = mid

    if acc[h+ok][w+ok] == acc[h+ng][w+ng]:
        return ok+1
    else:
        return ok


ans = 0

for h in range(H):
    for w in range(W):
        if (h, w) in s_holes:
            continue

        ans += my_bisect(h, w) + 1

print(ans)
