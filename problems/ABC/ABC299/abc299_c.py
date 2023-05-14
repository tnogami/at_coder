N = int(input())
S = input()
dango = S.split('-')
ans = 0

for d in dango:
    ans = max(ans, len(d))

if '-' not in S:
    print(-1)
else:
    print(ans) if ans else print(-1)