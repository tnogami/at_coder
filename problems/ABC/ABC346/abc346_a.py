N = int(input())
A = list(map(int,input().split()))
ans = []
for n in range(N-1):
    ans.append(A[n]*A[n+1])

print(*ans)