from collections import deque

INF = 10**18

def bfs(s, g):
    dist = [[-1 for i in range(W)] for j in range(H)] #距離
    dq = deque()
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)

    # 始点の設定
    dq.append(s)
    dist[s[0]][s[1]] = 0

    #キューが無くなるまでループ
    while dq:
        cur_y, cur_x = dq.popleft()

        for k in range(4):
            next_y, next_x = cur_y+dy[k], cur_x+dx[k]
            if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
            if field[next_y][next_x] == "#" : continue #壁
            if dist[next_y][next_x] != -1 : continue #訪問済み
            dist[next_y][next_x] = dist[cur_y][cur_x] + 1
            dq.append((next_y,next_x))

    return dist[g[0]][g[1]]

H, W, T = map(int, input().split())

field = [input() for _ in range(H)]

okashi = []
for j in range(H):
    for i in range(W):
        if field[j][i] == 'G':
            goal = (j,i)
        elif field[j][i] == 'S':
            start = (j,i)
        elif field[j][i] == 'o':
            okashi.append((j,i))


V = len(okashi)
from itertools import combinations

G = [[INF]*V for _ in range(V)]
s2o = [INF]*V
g2o = [INF]*V

direct = bfs(goal, start)

for i in range(V):
    d = bfs(start, okashi[i])
    if d != -1:
        s2o[i] = d

    d = bfs(goal, okashi[i])
    if d != -1:
        g2o[i] = d

for a, b in combinations(range(V), 2):
    d = bfs(okashi[a], okashi[b])
    if d != -1:
        G[a][b] = d
        G[b][a] = d
 
if direct == -1 or T < direct:
    print(-1)
else:

    # E = V*(V-1)//2
    # G = [[INF]*V for i in range(V)] # 存在しないパスはinfになるように、最初にすべてinfにしておく
    # for i in range(E):
    #     s,t,d = map(int,input().split())
    #     G[s][t] = d # s,tは0以上V-1以下なので、デクリメントの必要はない
    dp = [[INF]*V for i in range(2**V)] # dpの長さは2^V必要
    # dp[0][0] = 0 # 0から出発するのでdp[0][0]を0にしておく

    for S in range(2**V): # Sは集合をbitで表している
        for v in range(V): # vは配られる側の要素を表している
            for u in range(V): # uは配る側の要素を表している
                if S == 0: # 開始点はスタートからvへのコスト
                    dp[1 << v][v] = s2o[v]
                    continue
                if ((S >> u) & 1) and (((S >> v) & 1) == 0) : # 配る側のuが1で配られる側が0の場合のみ遷移する
                    if dp[S][u] + G[u][v] < dp[S | (1 << v)][v]:
                        dp[S | (1 << v)][v] = dp[S][u] + G[u][v] # ③

    ans = 0
    for i in range(2**V):
        for v in range(V):
            if dp[i][v] + g2o[v] <= T:
                ans = max(ans,  bin(i).count('1'))

    print(ans)
