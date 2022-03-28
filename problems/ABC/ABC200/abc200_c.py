from collections import defaultdict
d = defaultdict(int)

N = int(input())
A = list(map(int,input().split()))

ans = 0
for a in A:
    n = a%200
    ans += d[n]
    d[n] += 1

print(ans)