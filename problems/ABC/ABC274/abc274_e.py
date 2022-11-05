import math
import itertools
N, M = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]
PQ = [tuple(map(int, input().split())) for _ in range(M)]

XYPQ = XY+PQ
nodes = [[10**12]*(N+M) for _ in range(N+M)]

for i in range(N+M-1):
    for j in range(i, N+M):
        dist = (XYPQ[i][0]-XYPQ[j][0])**2 + (XYPQ[i][1]-XYPQ[j][1])**2
        nodes[i][j] = math.sqrt(dist)
        nodes[j][i] = math.sqrt(dist)

dp = [[10**12]*(N+M) for _ in range(2**(N+M))]

for i in range(N):
    s = 1<<i
    dp[s][i] = math.sqrt(XY[i][0]**2+XY[i][1]**2)

for i in range(M):
    s = 1<<(N+i)
    dp[s][N+i] = math.sqrt(PQ[i][0]**2+PQ[i][1]**2)

for s in range(2**(N+M)):
    boost_ct = 0
    tmp = (s>>N)
    for m in range(M):
        if ((tmp>>m)&1) == 1: boost_ct += 1
    for frm in range(N+M):
        for to in range(N+M):
            if ((s>>(frm))&1) == 0:continue
            if ((s>>(to))&1) == 1:continue

            dp[s|(1<<(to))][to] = min(dp[s|(1<<(to))][to], dp[s][frm]+nodes[frm][to]/2**boost_ct)

ans = 10**12
for i, d in enumerate(dp):
    flag = True
    for n in range(N):
        if (i>>n)&1 != 1:
            flag = False
            break

    boost_ct = 0
    tmp = (i>>N)
    for m in range(M):
        if ((tmp>>m)&1) == 1: boost_ct += 1
    
    if flag:
        for end, tmp in enumerate(d):
            ans = min(ans, tmp + math.sqrt(XYPQ[end][0]**2+XYPQ[end][1]**2)/2**boost_ct)

print(ans)
