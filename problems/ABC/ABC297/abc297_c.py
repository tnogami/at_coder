H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = []
for s in S:
    ans.append(s.replace('TT', 'PC'))

for a in ans:
    print(a)