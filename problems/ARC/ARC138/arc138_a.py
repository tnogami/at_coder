import bisect
N, K = map(int, input().split())
A = list(map(int,input().split()))

left = A[:K]
right = A[K:]

s = sum(left)

right = [(n,i) for i, n in enumerate(right)]
right.sort(key=lambda x:x[1])
right.sort()
B = list(map(lambda x : x[0], right))

ans = len(A) + 10
for i, n in enumerate(left):
    idx = bisect.bisect(B, n)
    if N-K <= idx: continue
    ans = min(K-1-i+right[idx][1]+1, ans)

if ans == len(A) + 10:
    print(-1)
else:
    print(ans)


