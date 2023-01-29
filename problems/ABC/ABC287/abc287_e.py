import sys
sys.setrecursionlimit(10**9)

def dfs(i, idx_list):
    if len(idx_list) == 1:
        ans[idx_list[0]] = i-1
        return

    next_idx_list = dict()
    for idx in idx_list:
        if len(S[idx]) <= i:
            ans[idx] = i
            continue
        alpha = S[idx][i]
        if alpha in next_idx_list:
            next_idx_list[alpha].append(idx)
        else:
            next_idx_list[alpha] = [idx]

    for l in next_idx_list.values():
        dfs(i+1, l)


N = int(input())
S = [input() for _ in range(N)]
ans = [0]*N

dfs(0, list(range(N)))

for a in ans:
    print(a)