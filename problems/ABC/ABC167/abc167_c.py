N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]
ans = 10**10
for n in range(2**N):
    skills = [0]*M
    price = 0
    for i in range(N):
        if (n >> i)&1 == 1:
            price += CA[i][0]
            for j in range(M):
                skills[j] += CA[i][j+1]
    
    if all([X<=s for s in skills]):
        ans = min(ans, price)

if ans == 10**10:
    print(-1)
else:
    print(ans)