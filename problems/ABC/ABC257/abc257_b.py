N, K, Q = map(int, input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))

for l in L:
    if A[l-1] == N:continue
    if l == K:
        A[l-1] += 1
    else:
        if A[l] == A[l-1] + 1 : continue
        A[l-1] += 1

print(*A)





