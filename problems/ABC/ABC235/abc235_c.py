from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int,input().split()))

d = defaultdict(list)
s = set()

for i , a in enumerate(A):
    d[a].append(i+1)
    s.add(a)


for _ in range(Q):
    x, k = map(int, input().split())
    if x not in s:
        print(-1)
    else:
        if len(d[x]) < k:
            print(-1)
        else:
            print(d[x][k-1])



