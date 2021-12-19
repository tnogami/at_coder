#bit全探索

# ０１の数(2^20 ≒ 10^6なので最大でもN=20程度)
# 3桁の場合 0b111= 7 なので range(8)=range(2**3)のループ
N = int(input())
for i in range(2**N): #01の組み合わせ
    for j in range(N):  # シフト回数ループ
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う1
            # j番目のbitが1のときの処理

#====================================================================================

#幅優先探索(グラフ)

import queue

N = int(input())
M = int(input())
dist = [-1 for i in range(N)] #距離
que = queue.Queue()
nodes = [[] for i in range(N)]

#nodeの入力
for i in range(M):
    a,b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

# 始点の設定
que.put(0)
dist[0] = 0

#キューが無くなるまでループ
while not que.empty():
    cur = que.get()
    
    for next_node in nodes[cur]:
        if dist[next_node] != -1 : continue
        que.put(next_node)
        dist[next_node] = dist[cur] + 1

print(dist)

#====================================================================================

#幅優先探索(グリッド)
import queue

Nx, Ny = map(int, input().split())
dist = [[-1 for i in range(Nx)] for j in range(Ny)] #距離
que = queue.Queue()
dx = (0,1,0,-1)
dy = (1,0,-1,0)

#fieldの入力
field = [input() for j in range(Ny)]

# 始点の設定
que.put((0,0))
dist[0][0] = 0

#キューが無くなるまでループ
while not que.empty():
    cur_y, cur_x = que.get()

    for k in range(4):
        next_y, next_x = cur_y+dy[k], cur_x+dx[k]
        if next_x < 0 or Nx <= next_x or next_y < 0 or Ny <= next_y : continue #マスの外
        if field[next_y][next_x] == "#" : continue #壁
        if dist[next_y][next_x] != -1 : continue #訪問済み
        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        que.put((next_y,next_x))

print(dist)

#====================================================================================

#深さ優先探索(グラフ)
import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    
    for j in nodes[i]:
        if visited[j] == True : continue
        dfs(j)

N = int(input())
M = int(input())
nodes = [[] for i in range(N)]
visited = [-1 for i in range(N)]

for i in range(M):
    a,b =  map(int,input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

dfs(0)

print(visited)

#====================================================================================

#尺取り法
#積がK以下の区間で最長のものを求める

N, K = map(int, input().split())
S = list(map(int, input().split()))

right = 0
product = 1
ans = 0
for left in range(N):
    while right < N and product * S[right] <=  K:#積がKになるまで、rightを右にずらしていく
        product *= S[right]
        right += 1
    
    #rightが行き詰まったので、最大値を更新
    ans = max(ans, right - left)
 
    if right == left:#left loopがrightにまで来たらrightを右に一つずらす　
        right += 1
    else: #次のループでleftが一つ進むので、最後尾の数で割っておく
        product /= S[left]

print(ans)

#和がK以下となる区間で最長のものを求める
right = 0
amount = 0
ans = 0
for left in range(N):
    while right < N and amount + S[right] <= K :#和がKになるまで、rightを右にずらしていく
        amount += S[right]
        right += 1
    
    #rightが行き詰まったので、最大値を更新
    ans = max(ans, right - left)
 
    if right == left:#left loopがrightにまで来たらrightを右に一つずらす　
        right += 1
    else: #次のループでleftが一つ進むので、最後尾の数で割っておく
        amount -= S[left]

print(ans)

#====================================================================================

#Union-Find木

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N = int(input())
uf = UnionFind(N)
uf.union(a, b) #辺を追加

#====================================================================================

#ワーシャル・フロイド法

N = int(input())
M = int(input())

dist = [[float("INF")]*N for i in range(N)]
for i in range(N): #自己への移動コストはゼロ
    dist[i][i] = 0
    
for i in range(M):
    a,b,t = map(int, input().split())
    dist[a-1][b-1] = t
    dist[b-1][a-1] = t

#ワーシャル・フロイド法でi-jの最小コストを計算
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

#====================================================================================

#ダイクストラ法

from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

#====================================================================================
#グリットのダイクストラ法
from heapq import heappush, heappop
INF = 10 ** 12

#移動コストcを引数にして、ゴールまでの最短距離をダイクストラ法で求める。
def dijkstra(c):
    dist = [[INF]*W for i in range(H)]
    seen = [[False]*W for i in range(H)]
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    hq = [(0, (sx, sy))] # (distance, node)
    dist[sy][sx] = 0
    while hq:
        _sx, _sy = heappop(hq)[1] # ノードを pop する
        seen[_sy][_sx] = True
        for k in range(4):
            new_sx = _sx + dx[k]
            new_sy = _sy + dy[k]
            if new_sx < 0 or W <= new_sx or new_sy < 0 or H <= new_sy: continue
            if field[new_sy][new_sx] == "#":
                cost = c
            else:
                cost = 1
            if seen[new_sy][new_sx] == False and dist[_sy][_sx] + cost < dist[new_sy][new_sx]:
                dist[new_sy][new_sx] = dist[_sy][_sx] + cost
                heappush(hq, (dist[new_sy][new_sx], (new_sx, new_sy)))
    return dist[gy][gx]

#入力
H, W, T = map(int, input().split())
field = [input() for i in range(H)]

#スタートとゴールの座標の確認
for i in range(H):
    for j in range(W):
        if field[i][j] == "S": sx,sy = j,i
        if field[i][j] == "G": gx,gy = j,i

#====================================================================================

#因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

prime_factorize(111111111111111111)

#====================================================================================

#逆元, nCk, nCr
n = 10 ** 9
k = 2 * 10 ** 5
mod = 10**9 + 7
 
modinv_table = [-1] * (k+1)
modinv_table[1] = 1
for i in range(2, k+1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans

binomial_coefficients(99,3)

#====================================================================================

#最小公倍数
import math
from functools import reduce
# 2数を受け取って最小公倍数を返す関数
def lcm(a, b):
    n= a*b // math.gcd(a, b)
    return int(n)

# リストを受け取って最小公倍数を返す関数
def my_lcm(nums):
        return reduce(lcm, nums)
    
l = [4,5,19]
my_lcm(l)

#====================================================================================

#最大公約数
from functools import reduce
def my_gcd(nums):
    return reduce(math.gcd, nums)

l = [24,36,48]
my_gcd(l)

#====================================================================================

#約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

make_divisors(42)

#====================================================================================
#配列に名前をつけて持つ方法

from collections import defaultdict

xtoy = defaultdict(list)

x = 10**3
y = 3
xtoy[x].append(y)
y = 4
xtoy[x].append(y)

#====================================================================================

#セグ木

#####segfunc#####
import math
def segfunc(x, y):
    return math.gcd(x, y) #最大公約数
    #return min(x,y) #最小値
    #return max(x,y) #最大値
    #return x*y #区間積
    #return x+y #区間和
#################

#####ide_ele#####
ide_ele = 0 #区間最大公約数
#ide_ele = float('inf') #最小値
#ide_ele = -float('inf') #最大値
#ide_ele = 0 #区間和
#ide_ele = 1 #区間積
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N = int(input())
A = list(map(int,input().split()))

seg = SegTree(A, segfunc, ide_ele)
seg.update(i, a) #i番目の要素をaに更新
seg.query(0,N) #区間最大公約数など

#====================================================================================
#平衡二分探索木
#L = 2**Kとして、0~L-2までの値を扱える
#find_rのRootはL-1を返す

class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def append(self, v):# v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1<<self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    #####
                    return
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)    
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None
    
Q = int(input())
N = 2**20
A = [-1]*N
BT = BalancingTree(20) # 0 ～ 2**20 までの要素を入れられるピボット木


#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================
#====================================================================================

            