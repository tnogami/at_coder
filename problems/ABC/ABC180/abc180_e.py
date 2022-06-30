N = int(input())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]
nodes = [[10**12]*N for _ in range(N)]

for i in range(N-1):
    for j in range(i, N):
        dist_x = abs(XYZ[i][0]-XYZ[j][0])
        dist_y = abs(XYZ[i][1]-XYZ[j][1])
        dist_c0 = max(0, XYZ[j][2]-XYZ[i][2])
        dist_c1 = max(0, XYZ[i][2]-XYZ[j][2])
        nodes[i][j] = dist_x+dist_y+dist_c0
        nodes[j][i] = dist_x+dist_y+dist_c1


dp = [[10**12]*(N+1) for _ in range(2**N)]
dp[1][1] = 0

for s in range(2**N):
    for frm in range(1,N+1):
        for to in range(1,N+1):
            if ((s>>(frm-1))&1) == 0:continue
            if ((s>>(to-1))&1) == 1:continue
            dp[s|(1<<(to-1))][to] = min(dp[s|(1<<(to-1))][to], dp[s][frm]+nodes[frm-1][to-1])

ans = 10**12
for i,d in enumerate(dp[2**N-1][1:]):
    ans = min(ans, d+nodes[i][0])

print(ans)
