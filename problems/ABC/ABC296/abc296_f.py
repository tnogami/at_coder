from collections import Counter

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



N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

bit = Bit(max(A)+1)
ct_sw_a = 0
for i, a in enumerate(A):
    ct_sw_a += i - bit.sum(a+1)
    bit.add(a, 1)

bit = Bit(max(B)+1)
ct_sw_b = 0
for i, a in enumerate(B):
    ct_sw_b += i - bit.sum(a+1)
    bit.add(a, 1)

ct_a = Counter(A)
ct_b = Counter(B)

is_ok = True
for k, v in ct_a.items():
    if k not in ct_b:
        is_ok = False
    else:
        if v != ct_b[k]:
            is_ok = False

if is_ok:
    if ct_sw_a % 2 == ct_sw_b % 2:
        print("Yes")
    else:
        if len(set(A)) == N:
            print("No")
        else:
            print("Yes")
else:
    print("No")
