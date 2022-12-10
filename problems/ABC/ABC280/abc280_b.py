N = int(input())
S = list(map(int,input().split()))
ans = []
cur = 0
for s in S:
    ans.append(s-cur)
    cur += s-cur

print(*ans)


