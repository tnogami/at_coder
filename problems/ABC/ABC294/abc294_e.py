L, N1, N2 = map(int, input().split())

L1 = [tuple(map(int,input().split())) for _ in range(N1)]
L2 = [tuple(map(int,input().split())) for _ in range(N2)]

L1 = L1[::-1]
L2 = L2[::-1]

ans = 0

v1, l1 = L1.pop()
v2, l2 = L2.pop()

cur1_top = l1
cur2_top = l2

cur1_bottom = 0
cur2_bottom = 0

while L1 or L2:
    if cur1_top < cur2_top:
        if v1 == v2:
            ans += min(cur1_top, cur2_top) - max(cur1_bottom, cur2_bottom)
        v1, l1 = L1.pop()
        cur1_bottom = cur1_top
        cur1_top += l1
    else:
        if v1 == v2:
            ans += min(cur1_top, cur2_top) - max(cur1_bottom, cur2_bottom)
        v2, l2 = L2.pop()
        cur2_bottom = cur2_top
        cur2_top += l2

if v1 == v2:
    ans += min(cur1_top, cur2_top) - max(cur1_bottom, cur2_bottom)

print(ans)