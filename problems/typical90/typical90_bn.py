N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        L1, R1 = LR[i]
        L2, R2 = LR[j]
        tmp = 0
        for m in range(L1, R1+1):
            for n in range(L2, R2+1):
                if n < m : tmp += 1

        ans += tmp/((R1-L1+1)*(R2-L2+1))

print(ans)