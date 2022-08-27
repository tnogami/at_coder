X, Y, N = map(int, input().split())
ans = 10000000
for a in range(100):
    tmp_cost = X*a
    for b in range(100):
        cost = tmp_cost + Y*b
        if a+3*b == N:
            ans = min(ans, cost)

print(ans)