N = int(input())
A = list(map(int, input().split()))
A.sort()
for i in range(N):
    if A[i] + 1 != A[i+1]:
        break
print(A[i]+1)
