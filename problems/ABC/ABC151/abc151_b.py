N, K, M = map(int, input().split())
A = list(map(int,input().split()))

s = sum(A)

req = N*M - s

if K < req:
    print(-1)
else:
    print(max(0, req))