import copy
N = int(input())
B = list(map(int,input().split()))

C = copy.copy(B)
C.sort()
a1 = C[N//2]
a2 = C[N//2-1]


for b in B:
    if a1 <= b:
        print(a2)
    else:
        print(a1)