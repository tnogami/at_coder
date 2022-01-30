N, L = map(int, input().split())
all_apple = N*L - N + N*(N+1)//2
diff = 100000000000000
ans = 0
for i in range(1,N+1):
    if diff > abs(L+i-1):
        diff = abs(L+i-1)
        ans = L+i-1
print(all_apple - ans)
    