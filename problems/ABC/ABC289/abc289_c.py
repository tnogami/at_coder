N, M = map(int, input().split())
Aset = []
for _ in range(M):
    C = int(input())
    A = set(map(int,input().split()))
    Aset.append(A)

ct = 0
correct_set = set(range(1,N+1))
for n in range(1, 2**M):
    tmp_set = set()
    for k in range(M):
        if ((n >> k) & 1) == 1:
            tmp_set |= Aset[k]
    if tmp_set == correct_set:ct += 1

print(ct)