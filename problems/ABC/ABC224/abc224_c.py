N = int(input())

XY = [tuple(map(int, input().split())) for i in range(N)]
ans = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            a1 = XY[j][0] - XY[i][0]
            b1 = XY[j][1] - XY[i][1]
            a2 = XY[k][0] - XY[i][0]
            b2 = XY[k][1] - XY[i][1]
            if a1*b2 - a2*b1 != 0 : ans += 1

print(ans)