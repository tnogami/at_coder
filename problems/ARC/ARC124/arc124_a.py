
N, K = map(int, input().split())

ans = [K for i in range(N)]

for i in range(K):
    c, k = input().split()
    k = int(k)
    ans[k-1] = 1
    if c == "L":
        for j in range(0, k-1):
            if ans[j]!=1:ans[j]-=1
    
    if c == "R":
        for j in range(k, N):
            if ans[j]!=1:ans[j]-=1

out = 1
for a in ans:
    out *= a
    out %= 998244353

print(out)