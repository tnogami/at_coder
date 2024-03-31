from collections import defaultdict
H, W, M = map(int, input().split())

d = defaultdict(int)

query = [tuple(map(int,input().split())) for _ in range(M)]

query = query[::-1]

done_ver = set()
num_ver = 0
done_hol = set()
num_hol = 0

for q in query:
    t, a, x = q
    if t == 1:
        if a in done_hol:
            continue

        done_hol.add(a)
        num_hol += 1
        d[x] += W - num_ver
    else:
        if a in done_ver:
            continue

        done_ver.add(a)
        num_ver += 1
        d[x] += H - num_hol

amount = sum(d.values())
if amount != H*W:
    add_zero = H*W-amount
    d[0] += add_zero

ans = [(k, v) for k, v in d.items() if v != 0]
ans.sort()

print(len(ans))
for a in ans:
    print(*a)