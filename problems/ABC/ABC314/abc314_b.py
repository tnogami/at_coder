N = int(input())
ct = [0]*N
bets = [[] for _ in range(37)]
for n in range(N):
    c = int(input())
    A = list(map(int, input().split()))
    ct[n] = c
    for a in A:
        bets[a].append(n+1)

X = int(input())

bet = bets[X]
tmp = []
for b in bet:
    tmp.append(ct[b-1])

if tmp:

    m = min(tmp)
    ans = []
    for b in bet:
        if ct[b-1] == m:
            ans.append(b)

    ans.sort()
    print(len(ans))
    print(*ans)
else:
    print(0)
