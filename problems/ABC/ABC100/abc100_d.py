N, M = map(int, input().split())
cakes = [tuple(map(int, input().split())) for i in range(N)]
ans = -10**10
for n in range(2**3):
    tmp = []
    for cake in cakes:
        cost = 0
        for j in range(3):
            if (n>>j)&1 == 1:
                cost += cake[j]
            else:
                cost -= cake[j]
        tmp.append(cost)
    tmp.sort(reverse=True)
    ans = max(ans, sum(tmp[:M]))

print(ans)



