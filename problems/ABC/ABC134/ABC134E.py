import bisect
N = int(input())
A = [int(input()) for i in range(N)]
ans = [-A[0]]
for i in range(1, N):
    if ans[-1] <= -A[i]:
        ans.append(-A[i])
    else:
        idx = bisect.bisect(ans, -A[i])
        ans[idx] = -A[i]
            
print(len(ans))