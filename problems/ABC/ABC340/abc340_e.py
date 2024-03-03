

def segfunc(x,y):
    return x+y
class LazySegTree_RAQ:
    def __init__(self,init_val,segfunc,ide_ele ):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [0]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v==0:
                continue
            self.lazy[i] = 0
            self.lazy[2*i] += v
            self.lazy[2*i+1] += v
            self.tree[2*i] += v
            self.tree[2*i+1] += v
    def add(self,l,r,x):
        ids = self.gindex(l,r)
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r&1:
                self.lazy[r-1] += x
                self.tree[r-1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1]) + self.lazy[i]
    def query(self,l,r):
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

init_val = A[:]

lst = LazySegTree_RAQ(init_val, segfunc, 0)

for b in B:
    # ballの数を取得
    n = lst.query(b, b+1)

    # 空にする
    lst.add(b, b+1, -n)
    
    # ballを入れ始めるindexを確認
    idx = (b + 1) % N

    # 何周回って配れるか
    n_rot = n // N
    
    # 余る分の数
    n_mod = n % N

    if n_rot != 0:
        lst.add(0, N, n_rot)

    if n_mod == 0:
        continue

    if N < idx + n_mod:
        lst.add(idx, N, 1)
        lst.add(0, n_mod - (N - idx), 1)
    else:
        lst.add(idx, idx + n_mod, 1)

ans = []

for i in range(N):
    ans.append(lst.query(i, i+1))

print(*ans)