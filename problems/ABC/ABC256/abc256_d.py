N = int(input())
LR = [tuple(map(int, input().split())) for _ in range(N)]
LR.sort()
LR.append((10**9,10**10))

st = 0
end = -5

ans = []

for l,r in LR:
    if end < l:
        ans.append((st,end))
        st = l
        end = r
    else:
        end = max(end,r)
    
for a in ans[1:]:
    print(*a)
