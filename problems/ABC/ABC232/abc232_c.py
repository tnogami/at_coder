import itertools
N, M = map(int, input().split())
takahashi = [set([]) for i in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    takahashi[A-1].add(B-1)
    takahashi[B-1].add(A-1)
    
himo = [tuple(map(int, input().split())) for i in range(M)]

tr = [i for i in range(N)]
for trans in itertools.permutations(tr):
    aoki = [set([]) for i in range(N)]
    for c, d in himo:
        aoki[trans[c-1]].add(trans[d-1])
        aoki[trans[d-1]].add(trans[c-1])
    if aoki == takahashi:
        print("Yes")
        break
else:
    print("No")








