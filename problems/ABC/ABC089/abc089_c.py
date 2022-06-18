from collections import defaultdict
N = int(input())
d = defaultdict(int)
init = set(["M","A","R","C","H"])
for _ in range(N):
    name = input()
    if name[0] in init:
        d[name[0]] += 1

m = sum(d.values())
ans = m*(m-1)*(m-2)//6

for k in d.values():
    ans -= k*(k-1)//2 * (m-k)

for k in d.values():
    ans -= k*(k-1)*(k-2)//6

print(ans)

