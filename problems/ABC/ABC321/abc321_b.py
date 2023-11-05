N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(101):
    B = A[:] + [i]
    B.sort()
    point = sum(B[1:-1])
    if X <= point:
        print(i)
        break
else:
    print(-1)
