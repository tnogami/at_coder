N = int(input())
A = list(map(int,input().split()))
A.sort()
A = A[N:-N]
print(sum(A)/(3*N))