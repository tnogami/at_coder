import bisect
N, K = map(int, input().split())
A = list(map(int,input().split()))

left = A[:K]
right = A[K:]

if max(right) <= min(left):
    print(-1)
else:
    m = 0
    tmp = []
    for n in right:
        if m < n:m = n
        tmp.append(m)

    ans = 10**15
    for i, n in enumerate(left):
        idx = bisect.bisect(tmp, n)
        if N-K <= idx: continue
        ans = min(K-i+idx, ans)

    print(ans)