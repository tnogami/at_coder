from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int,input().split()))

ans = [[True]*(N+1) for _ in range(M)]

for i, a in enumerate(A):
    i += 1
    if 0 <= a:
        first = 1
    else:
        first = -(-(-a)//i)

    if M < first:continue

    for m in range(first, M+1):
        f = i*m+a
        if N < f:break
        ans[m-1][f] = False

for a in ans:
    for i,t in enumerate(a):
        if t:
            print(i)
            break
