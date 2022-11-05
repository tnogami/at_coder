N, K, A = map(int, input().split())
ans = A - 1
for i in range(K-1):
    ans += 1
print(ans%N+1)