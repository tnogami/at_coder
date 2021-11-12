import itertools
N = int(input())
class1 = [0 for i in range(N+2)]
class2 = [0 for i in range(N+2)]

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        class1[i+1] = p
    else:
        class2[i+1] = p

acc1 = list(itertools.accumulate(class1))
acc2 = list(itertools.accumulate(class2))

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    p1 = acc1[R] - acc1[L-1]
    p2 = acc2[R] - acc2[L-1]
    print(p1, p2)