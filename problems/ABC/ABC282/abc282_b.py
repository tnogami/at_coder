import itertools
N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0
for comb in itertools.combinations(range(N), 2):
    is_ok = True
    i, j = comb
    for m in range(M):
        if S[i][m] == 'x' and S[j][m] == 'x':
            is_ok = False

    if is_ok: ans += 1


print(ans)