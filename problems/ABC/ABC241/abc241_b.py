import collections
N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ct_b = collections.Counter(A)
for a in B:
    if ct_b[a] == 0:
        print("No")
        break
    ct_b[a] -= 1
else:
    print("Yes")