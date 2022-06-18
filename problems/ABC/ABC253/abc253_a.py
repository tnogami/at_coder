A = list(map(int,input().split()))
if A[1] == list(sorted(A))[1]:
    print("Yes")
else:
    print("No")