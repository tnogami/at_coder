N, K = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

am = max(A)
idx = []

for i, a in enumerate(A):
    if a == am:
        idx.append(i+1)

for i in B:
    if i in idx:
        print("Yes")
        break
else:
    print("No")


