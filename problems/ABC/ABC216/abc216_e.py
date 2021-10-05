def al(n):
    return n*(n+1)//2

import bisect
N, K = map(int, input().split())
A = list(map(int,input().split()))
A.sort()
m = 0
N += 1
A = [0] + A

if sum(A) <= K:
    ans = 0
    for a in A:
        ans += al(a)
    print(ans)
else:
    ans = 0
    n = 1
    cur = A[-1]
    for i in range(K):
        idx = bisect.bisect_left(A, cur)
        n = N - idx
        t = (cur - A[idx-1]) * n
        if t < K:
            ans += ((cur + A[idx-1] + 1) * (cur - A[idx-1]))//2 * n
            cur = A[idx-1]
            K -= t
        else:
            i = K // n
            ans += (i * (cur+cur-i+1))//2 * n
            ans += (K-(i*n))*(cur-i)
            break
    print(ans)

