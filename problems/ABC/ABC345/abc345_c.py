from collections import defaultdict
S = list(input())
d = defaultdict(int)

for s in S:
    d[s] += 1


ans = (len(S)*(len(S)-1))//2
flag = False
for k, v in d.items():
    if v >= 2:
        ans -= (v*(v-1))//2
        flag = True

if flag:
    ans += 1
print(ans)