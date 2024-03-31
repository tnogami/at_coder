N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))

s = set()

for n in range(N):
    for m in range(M):
        for l in range(L):
            s.add(A[n]+B[m]+C[l])

for x in X:
    if x in s:
        print('Yes')
    else:
        print('No')