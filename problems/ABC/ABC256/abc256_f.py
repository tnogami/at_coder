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
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])


MOD = 998244353

N, Q = map(int, input().split())
A = list(map(int,input().split()))

BIT1 = Bit(N+2) #Ai
BIT2 = Bit(N+2) #i*Ai
BIT3 = Bit(N+2) #i**2*Ai

for i, a in enumerate(A):
    BIT1.add(i+1, a)
    BIT2.add(i+1, (i+1)*a)
    BIT3.add(i+1, (i+1)**2*a)

for _ in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        x, v = query[1], query[2]
        v1 = BIT1.sum(x+1)-BIT1.sum(x)
        v2 = BIT2.sum(x+1)-BIT2.sum(x)
        v3 = BIT3.sum(x+1)-BIT3.sum(x)

        BIT1.add(x, -v1+v)
        BIT2.add(x, -v2+x*v)
        BIT3.add(x, -v3+x**2*v)

    else:
        x = query[1]
        v1 = (x**2 + 3*x + 2) * BIT1.sum(x+1)
        v2 = (-2*x-3) * BIT2.sum(x+1)
        v3 = BIT3.sum(x+1)

        print(((v1+v2+v3)//2)%MOD)
