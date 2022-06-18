N = int(input())
F = [tuple(map(int,input().split())) for _ in range(N)]
P = [tuple(map(int,input().split())) for _ in range(N)]

ans = -10**18
for n in range(1,2**10): #全通り
    ct = [0]*N
    for i in range(10): #店が営業するか
        if (n>>i) & 1 == 1: #営業する
            for k,f in enumerate(F): #営業している店をカウント
                if f[i] == 1 : ct[k] += 1

    tmp = 0
    for i, c in enumerate(ct):
        tmp += P[i][c]

    ans = max(ans, tmp)

print(ans)
