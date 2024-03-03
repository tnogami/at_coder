N = int(input())

for i in range(N):
    A = list(map(int,input().split()))
    ans = []
    for i, a in enumerate(A, 1):
        if a == 1:
            ans.append(i)
    print(*ans)