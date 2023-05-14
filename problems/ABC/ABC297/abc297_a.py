N, D = map(int, input().split())
A = list(map(int,input().split()))

cur = A[0]

for a in A[1:]:
    if a - cur <= D:
        print(a)
        break
    cur = a
else:
    print(-1)