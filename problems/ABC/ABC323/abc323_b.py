N = int(input())
S = [input() for _ in range(N)]

wins = [0] * N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if S[i][j] == "o":
            wins[i] += 1

ans = []
for i, win in enumerate(wins):
    ans.append((win, i + 1))

ans.sort(key=lambda x: x[1])
ans.sort(key=lambda x: -x[0])

out = []
for a in ans:
    out.append(a[1])

print(*out)
