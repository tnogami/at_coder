N = int(input())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]

zsum = sum([z for x, y, z in XYZ])

obtained = 0
losed = []
for x, y, z in XYZ:
    if x > y:
        obtained += z
    else:
        losed.append((x, y, z))

if obtained > zsum//2:
    print(0)
    exit()
else:
    zreq = -(-zsum//2) - obtained

    # len(losed)番目まで見て、zreqを達成するための最小のコスト
    dp = [[10**18]*(zreq+1) for _ in range(len(losed)+1)]
    dp[0][0] = 0
    for i in range(len(losed)):
        x, y, z = losed[i]
        for j in range(zreq+1):
            # 鞍替えさせない場合
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            # 鞍替えさせる場合
            xreq = (x+y)//2 - x + 1
            if j+z >= zreq:
                dp[i+1][zreq] = min(dp[i+1][zreq], dp[i][j] + xreq)
            else:
                dp[i+1][j+z] = min(dp[i+1][j+z], dp[i][j] + xreq)

    print(dp[-1][-1])
