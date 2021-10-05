
from collections import defaultdict

per = defaultdict(list)

N = int(input())

for i in range(1,10):
    for j in range(1,10):
        per[str(i)+str(j)] = 0

for i in range(1, N+1):
    n = str(i)
    if n[-1] == "0" : continue
    h = n[0]
    t = n[-1]
    per[h+t] += 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        ans += per[str(i)+str(j)]*per[str(j)+str(i)]

print(ans)
