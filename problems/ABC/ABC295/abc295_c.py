from collections import Counter

N = int(input())
A = list(map(int,input().split()))

ct = Counter(A)
ans = 0
for k, v in ct.items():
    ans += v//2

print(ans)