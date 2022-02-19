#####segfunc#####
def segfunc(x, y):
    #return math.gcd(x, y) #最大公約数
    #return min(x,y) #最小値
    return max(x,y) #最大値
    #return x*y #区間積
    #return x+y #区間和
#################

#####ide_ele#####
#ide_ele = 0 #区間最大公約数
#ide_ele = float('inf') #最小値
ide_ele = -1 #最大値
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
        
W, N = map(int, input().split())

A = [-float("inf")]*(W+1)
seg = SegTree(A, segfunc, ide_ele)
dp = [[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
seg.update(0,0)

for n in range(N):
    L, R, V = map(int, input().split())
    for w in range(W, -1, -1):
        if w - L < 0:
            dp[n+1][w] = dp[n][w]
        else:
            st = max(0, w - R)
            end = max(1, w - L + 1)
            pre_state = seg.query(st,end)
            if pre_state == -1:
                dp[n+1][w] = dp[n][w]
            else:
                tmp = pre_state + V
                if tmp <= dp[n][w]:
                    dp[n+1][w] = dp[n][w]
                else:
                    dp[n+1][w] = tmp
                    seg.update(w, tmp)

if dp[N][W] < 0:
    print("-1")
else :
    print(dp[N][W])
