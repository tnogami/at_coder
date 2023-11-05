from bisect import bisect
N = int(input())
A = list(map(int, input().split()))

d = dict()

for i, a in enumerate(A):
    if a in d:
        d[a].append(i)
    else:
        d[a] = [i]

ans = 0
for k, l in d.items():
    n = len(l)
    for i in range(n-1):
        ans += (l[i+1] - l[i] - 1)*(i+1)*(n-i-1)

print(ans)
