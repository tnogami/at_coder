N = int(input())

ans = []
for n in range(1,N+1):
    out = []
    for j in range(n):
        if j == 0 or j == n-1:
            out.append(1)
        else:
            out.append(ans[n-2][j-1]+ans[n-2][j])
    ans.append(out)

for a in ans:
    print(*a)

