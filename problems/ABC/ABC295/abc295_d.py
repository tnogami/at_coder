from collections import defaultdict
S = input()
acc = [[0] for _ in range(10)]

for s in S:
    for i in range(10):
        if int(s) == i:
            acc[i].append(acc[i][-1]+1)
        else:
            acc[i].append(acc[i][-1])

d = defaultdict(int)

for i in range(len(S)+1):
    tmp = []
    for j in range(10):
        if acc[j][i] % 2 == 0:
            tmp.append('o')
        else:
            tmp.append('e')
    k = ''.join(tmp)
    d[k] += 1

ans = 0
for v in d.values():
    ans += (v*(v-1))//2
    
print(ans)