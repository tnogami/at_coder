a, b, C = map(int, input().split())

C_bin = bin(C)[2:]
C_bin = '0' * (60-len(C_bin)) + C_bin

ct_0 = 0 # 00と11の合計個数
ct_1 = 0 # 01と10の合計個数
for c in C_bin:
    if c == '0':
        ct_0 += 1
    else:
        ct_1 += 1

m = a + b # 1の合計数
n11 = (m - ct_1) // 2
n00 = ct_0 - n11
n01 = b - n11
n10 = a - n11

if m < ct_1:
    print(-1)
elif (m - ct_1) % 2 == 1:
    print(-1)
elif n00 < 0 or n01 < 0 or n10 < 0 or n11 < 0:
    print(-1)
else:
    n11 = (m - ct_1) // 2
    n00 = ct_0 - n11
    n01 = b - n11
    n10 = a - n11
    X = []
    Y = []
    # print(n11, n00, n01, n10)
    for c in C_bin:
        if c == '0': # 00 or 11
            if n11 > 0:
                a -= 1
                b -= 1
                n11 -= 1
                X.append('1')
                Y.append('1')
            else:
                n00 -= 1
                X.append('0')
                Y.append('0')
        else:
            if n01 > 0:
                n01 -= 1
                b -= 1
                X.append('0')
                Y.append('1')
            else:
                n10 -= 1
                a -= 1
                X.append('1')
                Y.append('0')
    # print(''.join(X), ''.join(Y))
    print(int(''.join(X), 2), int(''.join(Y), 2))




