
H, W = map(int, input().split())
field = [input() for _ in range(H)]
ans = [0]*min(H,W)

def check(i,j):
    ans = 1
    for k in range(1, 1000):
        if W <= i + k or H <= j + k : break
        if field[j+k][i+k] == '.' : break
        ans += 1
    return ans//2

for j in range(H):
    for i in range(W):
        if field[j][i] != '#': continue
        if j != 0 and i != 0 and field[j-1][i-1] == '#': continue
        idx = check(i,j)
        if idx == 0:continue
        ans[idx-1] += 1

print(*ans)