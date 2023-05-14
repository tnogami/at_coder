N = int(input())
A = list(map(int,input().split()))

ans = []
for i in range(N-1):
    ans.append(A[i])
    if A[i]+1 < A[i+1]:
        for k in range(A[i]+1,A[i+1]):
            ans.append(k)
    elif A[i]-1 > A[i+1]:
        for k in range(A[i]-1,A[i+1],-1):
            ans.append(k)

print(*ans)

