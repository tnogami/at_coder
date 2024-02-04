N, S, M, L = map(int, input().split())
ans = 10**12

for s in range(20):
    for m in range(20):
        for l in range(20):
            amount = 6*s + 8*m + 12*l
            if amount >= N:
                ans = min(ans, S*s+M*m+L*l)

print(ans)
