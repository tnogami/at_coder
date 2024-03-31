from itertools import product

V1, V2, V3 = map(int, input().split())

V_all = 3 * 7**3

# x:0-7, y:0-7, z:0-7の立方体
a1, b1, c1 = 0, 0, 0

def calc(a2, b2, c2, a3, b3, c3):
    # 1と2のx軸の共通部分
    x12 = max(0, min(a1+7, a2+7) - max(a1, a2))
    # 1と2のy軸の共通部分
    y12 = max(0, min(b1+7, b2+7) - max(b1, b2))
    # 1と2のz軸の共通部分
    z12 = max(0, min(c1+7, c2+7) - max(c1, c2))
    # 1と2の共通部分の体積
    v12 = x12 * y12 * z12        

    # 1と3のx軸の共通部分
    x13 = max(0, min(a1+7, a3+7) - max(a1, a3))
    # 1と3のy軸の共通部分
    y13 = max(0, min(b1+7, b3+7) - max(b1, b3))
    # 1と3のz軸の共通部分
    z13 = max(0, min(c1+7, c3+7) - max(c1, c3))
    # 1と3の共通部分の体積
    v13 = x13 * y13 * z13

    # 2と3のx軸の共通部分
    x23 = max(0, min(a2+7, a3+7) - max(a2, a3))
    # 2と3のy軸の共通部分
    y23 = max(0, min(b2+7, b3+7) - max(b2, b3))
    # 2と3のz軸の共通部分
    z23 = max(0, min(c2+7, c3+7) - max(c2, c3))
    # 2と3の共通部分の体積
    v23 = x23 * y23 * z23

    # 1, 2の共通部分の座標
    if v12 != 0:
        x12_min = max(a1, a2)
        y12_min = max(b1, b2)
        z12_min = max(c1, c2)
        x12_max = min(a1+7, a2+7)
        y12_max = min(b1+7, b2+7)
        z12_max = min(c1+7, c2+7)
        # 3との共通部分の体積
        x123 = max(0, min(x12_max, a3+7) - max(x12_min, a3))
        y123 = max(0, min(y12_max, b3+7) - max(y12_min, b3))
        z123 = max(0, min(z12_max, c3+7) - max(z12_min, c3))
        v123 = x123 * y123 * z123
    else:
        v123 = 0

    # 3つに含まれる部分の体積
    v3 = v123
    # 2つに含まれる部分の体積
    v2 = v12 + v23 + v13 - 3*v123
    # 1つに含まれる部分の体積
    v1 = V_all + 3*v123 - 2*v12 - 2*v23 - 2*v13
    return v1, v2, v3

#0-7まで
for a2, b2, c2 in product(range(-1, 8), repeat=3):
    for a3, b3, c3 in product(range(-1, 8), repeat=3):
        v1, v2, v3 = calc(a2, b2, c2, a3, b3, c3)
        if v1 == V1 and v2 == V2 and v3 == V3:
            print('Yes')
            print(a1, a2, a3, b1, b2, b3, c1, c2, c3)
            exit()
print('No')


