from collections import defaultdict

N, M = map(int, input().split())
ACed = set()
penalties = defaultdict(int)
ans = [0,0]
for _ in range(M):
    p, s = input().split()

    if s == "AC":
        if p in ACed:continue
        ans[0] += 1
        ans[1] += penalties[p]
        ACed.add(p)
    else:
        penalties[p] += 1

print(*ans)