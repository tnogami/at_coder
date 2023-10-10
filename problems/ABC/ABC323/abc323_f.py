Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

mx = Xc - Xb
my = Yc - Yb

ans = abs(mx) + abs(my)

if abs(mx) == 0:
    startx = Xb
    starty = Yb - 1 if my > 0 else Yb + 1

    if Xa == startx and (starty < Yb < Ya or Ya < Yb < starty):
        ans += 2

    ans += abs(Xa - startx)
    ans += abs(Ya - starty)

elif abs(my) == 0:
    startx = Xb - 1 if mx > 0 else Xb + 1
    starty = Yb

    if Ya == starty and (startx < Xb < Xa or Xa < Xb < startx):
        ans += 2

    ans += abs(Xa - startx)
    ans += abs(Ya - starty)

else:
    # 候補1
    dist1 = 0
    startx1 = Xb - 1 if mx > 0 else Xb + 1
    starty1 = Yb

    if Ya == starty1 and (startx1 < Xb < Xa or Xa < Xb < startx1):
        dist1 += 2

    dist1 += abs(Xa - startx1)
    dist1 += abs(Ya - starty1)

    # 候補2
    dist2 = 0
    startx2 = Xb
    starty2 = Yb - 1 if my > 0 else Yb + 1

    if Xa == startx2 and (starty2 < Yb < Ya or Ya < Yb < starty2):
        dist2 += 2

    dist2 += abs(Xa - startx2)
    dist2 += abs(Ya - starty2)

    ans += min(dist1, dist2)
    ans += 2

print(ans)
