N = int(input())
H = list(map(int,input().split()))

m = H[0]
ans = 1
for i in range(1,N):
    if m<=H[i]:
        ans += 1
    m = max(m, H[i])

print(ans)


