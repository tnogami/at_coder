from collections import Counter
N, K = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0
for n in range(2**N):
    ct = Counter()
    for i in range(N):
        if (n>>i)&1 == 1:
            for c in S[i]:
                ct[c] += 1

    tmp = 0
    for t, k in ct.items():
        if k == K:
            tmp += 1
    ans = max(tmp,ans)

print(ans)
    