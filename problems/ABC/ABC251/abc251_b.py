from itertools import combinations
N, W = map(int, input().split())
A = list(map(int,input().split()))
nset = set()
for i in range(1,4):
    for p in combinations(range(N), i):
        tmp = 0
        for k in p:
            tmp += A[k]
        if tmp <= W: nset.add(tmp)

print(len(nset))
