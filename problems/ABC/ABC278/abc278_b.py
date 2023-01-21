h, m = map(int, input().split())

while True:
    H = str(h).zfill(2)
    M = str(m).zfill(2)

    if 0 <= int(H[0]+M[0]) <=23 and 0 <= int(H[1]+M[1]) <=59:
        print(H, M)
        break

    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
