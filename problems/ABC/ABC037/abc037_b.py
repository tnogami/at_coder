N, Q = map(int, input().split())
ans = [0 for i in range(N)]
for i in range(Q):
    L, R, T = map(int, input().split())
    for i in range(L-1, R):
        ans[i] = T

for a in ans:
    print(a)
