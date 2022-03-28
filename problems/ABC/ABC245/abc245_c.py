import copy
N, K = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cur = set([A[0], B[0]])

for i in range(1, N):
    next_set = set()
    for c in cur:
        if abs(B[i]-c) <= K:
            next_set.add(B[i])
        if abs(A[i]-c) <= K:
            next_set.add(A[i])
    if len(next_set) == 0:
        print("No")
        break
    cur = copy.copy(next_set)
else:
    print("Yes")