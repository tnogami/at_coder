N, K, Q = map(int, input().split())
ans = [0 for i in range(N)]
for i in range(Q):
    a = int(input())
    ans[a-1] += 1

for i in range(N):
    if 0 < K-Q+ans[i]:
        print("Yes")
    else:
        print("No")