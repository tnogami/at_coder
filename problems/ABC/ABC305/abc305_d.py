import bisect 
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]
acc = [0]
total = 0
for i, a in enumerate(A[1:],1):
    if i%2 == 1:
        start_sleep = a
    else:
        total = total+(a-start_sleep)
        acc.append(total)

for query in queries:
    l, r = query
    idx_l = bisect.bisect(A, l)
    idx_r = bisect.bisect(A, r)

    if idx_l == idx_r:
        if idx_r % 2 == 0:
            print(r-l)
        else:
            print(0)

    else:
        ans = 0
        if idx_l % 2 == 0:
            ans -= l - A[idx_l-1]
        
        if idx_r % 2 == 0:
            ans += r - A[idx_r-1]

        ans += acc[(idx_r-1)//2] - acc[(idx_l-1)//2]
        print(ans)

