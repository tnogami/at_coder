N = int(input())
P = list(map(int,input().split()))
Q = int(input())

d = dict()
for i, p in enumerate(P):
    d[p] = i+1

for i in range(Q):
    a, b = map(int,input().split())
    if d[a] < d[b]:
        print(a)
    else:
        print(b)
