N = int(input())
A = list(map(int,input().split()))

cur = 1
ans = 0

for a in A:
    if a != cur:
        ans += 1
    else:
        cur += 1

if ans == N:
    print(-1)
else:
    print(ans)