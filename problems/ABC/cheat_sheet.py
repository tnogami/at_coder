# bit全探索

# ０１の数(2^20 ≒ 10^6なので最大でもN=20程度)
# 3桁の場合 0b111= 7 なので range(8)=range(2**3)のループ
from functools import cmp_to_key
from heapq import heappop, heappush
import heapq
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
from bisect import bisect_left, bisect_right, insort
from functools import reduce
import math
from heapq import heappush, heappop
from collections import defaultdict
import sys
from collections import deque
N = int(input())
for i in range(2**N):  # 01の組み合わせ
    for j in range(N):  # シフト回数ループ
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う1
            pass
            # j番目のbitが1のときの処理

# ====================================================================================

# 幅優先探索(グラフ)

N = int(input())
M = int(input())
A = list(map(int, input().split()))
nodes = [[] for _ in range(N)]

# nodeの入力
for i in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

dist = [-1 for i in range(N)]  # 距離

dq = deque()

# 始点の設定
dq.append(0)
dist[0] = 0

# キューが無くなるまでループ
while dq:
    cur = dq.popleft()

    for next_node in nodes[cur]:
        if dist[next_node] != -1:
            continue
        dq.append(next_node)
        dist[next_node] = dist[cur] + 1


# ====================================================================================

# 幅優先探索(グリッド)

Nx, Ny = map(int, input().split())
dist = [[-1 for i in range(Nx)] for j in range(Ny)]  # 距離
dq = deque()
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

# fieldの入力
field = [input() for j in range(Ny)]

# 始点の設定
dq.append((0, 0))
dist[0][0] = 0

# キューが無くなるまでループ
while dq:
    cur_y, cur_x = dq.popleft()

    for k in range(4):
        next_y, next_x = cur_y+dy[k], cur_x+dx[k]
        if next_x < 0 or Nx <= next_x or next_y < 0 or Ny <= next_y:
            continue  # マスの外
        if field[next_y][next_x] == "#":
            continue  # 壁
        if dist[next_y][next_x] != -1:
            continue  # 訪問済み
        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        dq.append((next_y, next_x))

print(dist)

# ====================================================================================

# 深さ優先探索(グラフ)
sys.setrecursionlimit(10**9)


def dfs(i):
    visited[i] = True

    for j in nodes[i]:
        if visited[j] == True:
            continue
        dfs(j)


N = int(input())
M = int(input())
nodes = [[] for i in range(N)]
visited = [-1 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

dfs(0)

print(visited)

# ====================================================================================

# 尺取り法
# 積がK以下の区間で最長のものを求める

N, K = map(int, input().split())
S = list(map(int, input().split()))

right = 0
product = 1
ans = 0
for left in range(N):
    while right < N and product * S[right] <= K:  # 積がKになるまで、rightを右にずらしていく
        product *= S[right]
        right += 1

    # rightが行き詰まったので、最大値を更新
    ans = max(ans, right - left)

    if right == left:  # left loopがrightにまで来たらrightを右に一つずらす　
        right += 1
    else:  # 次のループでleftが一つ進むので、最後尾の数で割っておく
        product /= S[left]

print(ans)

# 和がK以下となる区間で最長のものを求める
right = 0
amount = 0
ans = 0
for left in range(N):
    while right < N and amount + S[right] <= K:  # 和がKになるまで、rightを右にずらしていく
        amount += S[right]
        right += 1

    # rightが行き詰まったので、最大値を更新
    ans = max(ans, right - left)

    if right == left:  # left loopがrightにまで来たらrightを右に一つずらす　
        right += 1
    else:  # 次のループでleftが一つ進むので、最後尾の数で割っておく
        amount -= S[left]

print(ans)

# deque版尺取法
ans = 0
q = deque()
p = 1  # 今、見ている区間の要素の積をpで管理する。
for c in a:
    q.append(c)  # dequeの"右端"に要素を一つ追加する。
    p *= c

    while q and p > k:  # 要素の積がKを超えているか？
        rm = q.popleft()  # 条件を満たさないのでdequeの"左端"から要素を取り除く
        p //= rm  # 取り除いた値に応じて要素の積を更新する

    ans = max(ans, len(q))  # dequeに入っている要素の積がK以下になるまで区間を縮めた。

print(ans)

# ====================================================================================

# Union-Find木


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

    def members(self, x):  # 結構遅い
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
uf.union(a, b)  # 辺を追加

# ====================================================================================

# ワーシャル・フロイド法
# float('INF')は遅いので10**15とかにしたほうが良い
# 3000msの制限の問題で2200ms->800msになった

N = int(input())
M = int(input())

dist = [[float("INF")]*N for i in range(N)]
for i in range(N):  # 自己への移動コストはゼロ
    dist[i][i] = 0

for i in range(M):
    a, b, t = map(int, input().split())
    dist[a-1][b-1] = t
    dist[b-1][a-1] = t

# ワーシャル・フロイド法でi-jの最小コストを計算
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


# 経路復元
# dist_oldは最短経路計算前のグラフ
dist_old = []


def restore_path(start, end):
    p = []
    cur = start
    while (cur != end):
        for i in range(N):
            # (curr)---h[curr][i]---(i)---g[i][end]---(end)
            # と
            # (curr)-----------g[curr][end]-----------(end)
            # が一致すれば、iは最短経路に含まれる頂点である
            if i != cur and dist_old[cur][i] + dist[i][end] == dist[cur][end]:
                cur = i
                p.append(i)
                break

    return p

# ====================================================================================


# ダイクストラ法
adj = []
INF = 10 ** 21


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        cost, v = heappop(hq)  # ノードを pop する
        if seen[v]:
            continue
        seen[v] = True
        if dist[v] < cost:
            continue
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


def dijkstra(s, n, c_list):
    _list = [float("Inf")]*n
    _list[s] = 0
    hq = [[0, s]]
    heapq.heapify(hq)
    while len(hq) > 0:
        _ci, _i = heapq.heappop(hq)
        if _list[_i] < _ci:
            continue
        # ここに来たらノード_iまでのコストは確定
        for _cj, _j in c_list[_i]:
            if _list[_j] > (_list[_i] + _cj):
                _list[_j] = _list[_i] + _cj
                heapq.heappush(hq, [_list[_j], _j])
    return _list


# ====================================================================================
# グリットのダイクストラ法
INF = 10 ** 12

# 移動コストcを引数にして、ゴールまでの最短距離をダイクストラ法で求める。


def dijkstra(c):
    dist = [[INF]*W for i in range(H)]
    seen = [[False]*W for i in range(H)]
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    hq = [(0, (sx, sy))]  # (distance, node)
    dist[sy][sx] = 0
    while hq:
        _sx, _sy = heappop(hq)[1]  # ノードを pop する
        if seen[_sy][_sx]:
            continue
        seen[_sy][_sx] = True
        for k in range(4):
            new_sx = _sx + dx[k]
            new_sy = _sy + dy[k]
            if new_sx < 0 or W <= new_sx or new_sy < 0 or H <= new_sy:
                continue
            if field[new_sy][new_sx] == "#":
                cost = c
            else:
                cost = 1
            if seen[new_sy][new_sx] == False and dist[_sy][_sx] + cost < dist[new_sy][new_sx]:
                dist[new_sy][new_sx] = dist[_sy][_sx] + cost
                heappush(hq, (dist[new_sy][new_sx], (new_sx, new_sy)))
    return dist[gy][gx]


# 入力
H, W, T = map(int, input().split())
field = [input() for i in range(H)]

# スタートとゴールの座標の確認
for i in range(H):
    for j in range(W):
        if field[i][j] == "S":
            sx, sy = j, i
        if field[i][j] == "G":
            gx, gy = j, i

# ====================================================================================

# 素因数分解


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

# ====================================================================================

# 逆元, nCk, nCr mod p


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

print(cmb(n, r, p))

# ====================================================================================

# 最小公倍数
# 2数を受け取って最小公倍数を返す関数


def lcm(a, b):
    n = a*b // math.gcd(a, b)
    return int(n)

# リストを受け取って最小公倍数を返す関数


def my_lcm(nums):
    return reduce(lcm, nums)


l = [4, 5, 19]
my_lcm(l)

# ====================================================================================

# 最大公約数


def my_gcd(nums):
    return reduce(math.gcd, nums)


l = [24, 36, 48]
my_gcd(l)

# ====================================================================================

# 約数列挙


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


make_divisors(42)

# ====================================================================================
# 配列に名前をつけて持つ方法


xtoy = defaultdict(list)

x = 10**3
y = 3
xtoy[x].append(y)
y = 4
xtoy[x].append(y)

# ====================================================================================

# セグ木

##### segfunc#####


def segfunc(x, y):
    return math.gcd(x, y)  # 最大公約数
    # return min(x,y) #最小値
    # return max(x,y) #最大値
    # return x*y #区間積
    # return x+y #区間和
#################


##### ide_ele#####
ide_ele = 0  # 区間最大公約数
# ide_ele = float('inf') #最小値
# ide_ele = -float('inf') #最大値
# ide_ele = 0 #区間和
# ide_ele = 1 #区間積
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
A = list(map(int, input().split()))

seg = SegTree(A, segfunc, ide_ele)
seg.update(i, a)  # i番目の要素をaに更新
seg.query(0, N)  # 区間最大公約数など

# ====================================================================================
# 平衡二分探索木
# L = 2**Kとして、0~L-2までの値を扱える
# find_rのRootはL-1を返す


class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1 << n, 1 << n)

    def append(self, v):  # v を追加（その時点で v はない前提）
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
                        nd.left = self.node(mi, p - (p & -p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p)//2)
                        break

    def leftmost(self, nd):
        if nd.left:
            return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right:
            return self.rightmost(nd.right)
        return nd

    def find_l(self, v):  # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v:
            prev = nd.value
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

    def find_r(self, v):  # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v:
            prev = nd.value
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
        return self.find_l((1 << self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd=None, prev=None):  # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd:
            nd = self.root
        if not prev:
            prev = nd
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
BT = BalancingTree(20)  # 0 ～ 2**20 までの要素を入れられるピボット木


# ====================================================================================
# 2次元行列の転置
l_2d = [[1, 2, 3], [4, 5, 6]]
l_2d_t_tuple = list(zip(*l_2d))

# ====================================================================================
# SortedMultiSet

T = TypeVar('T')


class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size: size *
                    (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x:
            return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0:
            self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError
        for a in self.a:
            if x < len(a):
                return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


# ====================================================================================
# 1次元座標圧縮

N = map(int, input().split())
X = list(map(int, input().split()))

# 集合型にすることで重複を除去し、
# 小さい順にソートする
X_sorted = sorted(set(X))

# B の各要素が何番目の要素なのかを辞書型で管理する
Dx = {v: i for i, v in enumerate(X_sorted)}

# 答え
print([Dx[x] for x in X])

# ====================================================================================
# 2次元座標圧縮

N = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

# 集合型にすることで重複を除去し、
# 小さい順にソートする
X = sorted(set([a[0] for a in XY]))
Y = sorted(set([a[1] for a in XY]))

# B の各要素が何番目の要素なのかを辞書型で管理する
Dx = {v: i for i, v in enumerate(X)}
Dy = {v: i for i, v in enumerate(Y)}


# 答え
print(list(map(lambda x: (Dx[x[0]], Dy[x[1]]), XY)))

# ====================================================================================
# 転倒数


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size):
            raise ValueError("error!")
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size):
            raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size):
            raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size):
            raise IndexError("error!")
        self.add(key, value - self[key])


A = [3, 10, 1, 8, 5, 5, 1]
bit = Bit(max(A)+1)
ans = 0
for i, a in enumerate(A):
    ans += i - bit.sum(a+1)
    bit.add(a, 1)
print(ans)
# ====================================================================================

# 2次元累積和


def dim2imos(A: list) -> list:
    from itertools import accumulate
    ret = []
    for a in A:
        ret.append(list(accumulate(a)))
    for i in range(len(ret)-1):
        ret[i+1] = [ret[i][j]+ret[i+1][j] for j in range(len(ret[i]))]
    return ret

# ====================================================================================


# ローマ数字から数値1の変換
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        pre = -1
        for c in s[::-1]:
            if d[c] < pre:
                ret -= d[c]
            else:
                ret += d[c]
            pre = d[c]
        return ret


# 数字からローマ数字への変換
d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}


class Solution:
    def intToRoman(self, num: int) -> str:
        ret = []
        num = str(num)
        for i, n in enumerate(num[::-1]):
            n = int(n)
            m = n * 10**i
            if n == 9:
                c = d[10**i]+d[10**(i+1)]
            elif 5 <= n:
                c = d[5*10**i]+d[10**i]*(n-5)
            elif n == 4:
                c = d[10**i]+d[(n+1)*10**i]
            else:
                c = d[10**i]*n

            ret.append(c)

        return "".join(ret[::-1])


# ====================================================================================
# 強連結成分分解
sys.setrecursionlimit(10**9)


def SCC(N, G, rG):
    group_num = 0
    visited_order = []
    group = defaultdict(int)
    groups = []

    def dfs(i):
        seen[i] = True
        for to in G[i]:
            if seen[to]:
                continue
            dfs(to)
        visited_order.append(i)

    def r_dfs(i):
        seen[i] = True
        s.append(i)
        group[i] = group_num
        for to in rG[i]:
            if seen[to]:
                continue
            r_dfs(to)

    seen = [False]*N
    for i in range(N):
        if not seen[i]:
            dfs(i)

    seen = [False]*N
    for i in visited_order[::-1]:
        if not seen[i]:
            s = []
            r_dfs(i)
            groups.append(s)
            group_num += 1

    ret_G = [set([]) for _ in range(group_num)]
    for i in range(N):
        frm = group[i]
        for to in G[i]:
            if frm == group[to]:
                continue
            ret_G[frm].add(group[to])

    return groups, ret_G


G = [[1], [2], [3, 5, 8], [4, 5], [1], [6], [8], [6], [7]]
N = 9
groups, graph = SCC(9, G, rG)
print(groups)
print(graph)

# ====================================================================================
# 素数列挙


def f_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


# ====================================================================================
# 二部グラフの判定
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

nodes = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
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

# ====================================================================================
# トポロジカルソート
# DAGで有ることは前提として、hqを用いて辞書順最小のリストを返す


N, M = map(int, input().split())

out_list = [set() for _ in range(N)]
in_list = [set() for _ in range(N)]
inc = [0]*N
XY = set([tuple(map(int, input().split())) for _ in range(M)])
for x, y in XY:
    x -= 1
    y -= 1
    out_list[x].add(y)
    inc[y] += 1

S = []
L = []
for i, c in enumerate(inc):
    if c == 0:
        heappush(S, i)

while S:
    n = heappop(S)
    L.append(n)
    for m in out_list[n]:
        inc[m] -= 1
        if inc[m] == 0:
            heappush(S, m)

print(L)
# ====================================================================================
# 巡回セールスマン問題（bitDP）
# O(2**N * N**2)
# スタートとゴールが別にあり、スタートから各ノードを巡回する問題
INF = 10**18

V = 18  # ノード数
E = V*(V-1)//2  # エッジ数
G = [[INF]*V for _ in range(V)]  # 存在しないパスはinfになるように、最初にすべてinfにしておく
for i in range(E):  # 各ノード間の距離入力
    s, t, d = map(int, input().split())
    G[s][t] = d  # s,tは0以上V-1以下なので、デクリメントの必要はない

# スタートから各ノードへのコストはゼロ
goal2node = [0]*V
start2node = [0]*V

dp = [[INF]*V for i in range(2**V)]  # dpの長さは2^V必要

for S in range(2**V):  # Sは集合をbitで表している
    for v in range(V):  # vは配られる側の要素を表している
        for u in range(V):  # uは配る側の要素を表している
            if S == 0:  # 開始点はスタートからvへのコスト
                dp[1 << v][v] = start2node[v]
                continue
            if ((S >> u) & 1) and (((S >> v) & 1) == 0):  # 配る側のuが1で配られる側が0の場合のみ遷移する
                if dp[S][u] + G[u][v] < dp[S | (1 << v)][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + G[u][v]  # ③

# ====================================================================================

# 三角形の内外判定


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def is_inside_triangle(x1, y1, x2, y2, x3, y3, px, py):
    # Calculate the total area of the triangle
    total_area = area(x1, y1, x2, y2, x3, y3)

    # Calculate the areas of three sub-triangles formed by the point and the triangle vertices
    area1 = area(px, py, x2, y2, x3, y3)
    area2 = area(x1, y1, px, py, x3, y3)
    area3 = area(x1, y1, x2, y2, px, py)

    # If the sum of the areas of the sub-triangles is equal to the total area, the point is inside the triangle
    return area1 + area2 + area3 == total_area

# ====================================================================================
# ソートのキーを渡す
# ここでは分数のソートを行う


def cmp(a, b):  # a = [x_a, y_a], b = [x_b / y_b]
    # 比較対象の分数 a と b が等しければ 0 を返す
    if a[0] * b[1] == b[0] * a[1]:
        return 0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] < b[0] * a[1] else 1


N = int(input())

AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

ans = sorted(AB, key=cmp_to_key(cmp), reverse=True)
