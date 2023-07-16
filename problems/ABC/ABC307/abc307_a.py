N = int(input())

A = list(map(int, input().split()))

ct = 0
s = 0
ans = []
for i, a in enumerate(A):
    ct += 1
    s += a

    if ct == 7:
        ans.append(s)
        s = 0
        ct = 0

print(*ans)
