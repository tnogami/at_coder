N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = dict()

A_set = set(A)

for mex in range(N):
    if mex not in A_set:
        break


for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

for _ in range(Q):
    i, x = map(int, input().split())
    a = A[i-1]
    A[i-1] = x
    d[a] -= 1
    if d[a] == 0:
        del d[a]
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

    if a < mex and a not in d:
        mex = a
    elif mex in d and mex-1 not in d:
        mex -= 1
    elif mex in d and mex-1 in d:
        for mex in range(mex, 10**6):
            if mex not in d:
                break
    elif mex not in d and mex-1 in d:
        mex = mex
    elif mex not in d and mex-1 not in d:
        for tmp_mex in range(mex, -1, -1):
            if tmp_mex in d:
                mex = tmp_mex+1
                break
    print(mex)
