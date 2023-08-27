M = int(input())
D = list(map(int, input().split()))
s = sum(D)
center = -(-s//2)

ct = 0
for m in range(M):
    for d in range(D[m]):
        ct += 1
        if ct == center:
            mm = m+1
            dd = d+1

print(mm, dd)
