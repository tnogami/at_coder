from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i, a in enumerate(A):
    target = a + M
    idx = bisect_left(A, target)
    ans = max(ans, idx-i)

print(ans)
