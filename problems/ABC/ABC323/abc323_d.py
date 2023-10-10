from heapq import heappop, heappush

N = int(input())
slimes_ct = dict()

hq = []

for _ in range(N):
    s, c = map(int, input().split())
    slimes_ct[s] = c
    heappush(hq, s)


while hq:
    s1 = heappop(hq)
    if slimes_ct[s1] < 2:
        continue

    new_s = s1 * 2
    new_c = slimes_ct[s1] // 2
    slimes_ct[s1] -= new_c * 2

    if new_s in slimes_ct:
        slimes_ct[new_s] += new_c
    else:
        slimes_ct[new_s] = new_c
        heappush(hq, new_s)

ans = sum([c for c in slimes_ct.values()])

print(ans)
