import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 二部グラフの判定

nodes = [[] for _ in range(N)]

for m in range(M):
    u, v = A[m], B[m]
    u -= 1
    v -= 1
    nodes[u].append(v)
    nodes[v].append(u)

# n個の頂点の色を初期化。0:未着色、1:黒、-1:白
colors = [0 for i in range(N)]

# 頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse


def dfs(v, color):
    # 今いる点を着色
    colors[v] = color
    # 今の頂点から行けるところをチェック
    for to in nodes[v]:
        # 同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        # 未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    # 調べ終わったら矛盾がないのでTrue
    return True

# 2部グラフならTrue, そうでなければFalse


def is_bipartite():
    global colors
    ret = True
    c = 1
    for i in range(N):
        if colors[i] == 0:
            ret = ret and dfs(i, c)  # 頂点0を黒(1)で塗ってDFS開始
            c += 1
    return ret


if is_bipartite():
    print("Yes")
else:
    print("No")
