import math
N, M = map(int, input().split())

ans = 10**18
for a in range(1, max(10**6+100, int(math.sqrt(N))+10)):
    if N < a:
        break
    req = M // a
    m = req * a

    if req <= N and M <= m:
        ans = min(ans, m)
    
    req += 1
    m = req * a
    if req <= N and M <= m:
        ans = min(ans, m)


if ans == 10**18:
    print(-1)
else:
    print(ans)
