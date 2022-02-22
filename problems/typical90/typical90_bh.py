import bisect

def Lis(A, ret):
    L = [A[0]]
    ret.append(1)
    for a in A[1:]:
        if L[-1] < a:
            L.append(a)
        else:
            L[bisect.bisect_left(L,a)] = a
        ret.append(len(L))
    return ret

N = int(input())
A = list(map(int,input().split()))

L1 = []
L2 = []

Lis(A, L1)
Lis(A[::-1], L2)

ans = 0
for i in range(N):
    idx1 = i
    idx2 = N-1-i
    ans = max(ans, L1[idx1]+L2[idx2]-1)

print(ans)