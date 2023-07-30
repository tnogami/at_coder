N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = []
for i in range(N - 8):
    for j in range(M - 8):
        if S[i][j : j + 3] == "###":
            if (
                S[i + 1][j : j + 3] == "###"
                and S[i + 2][j : j + 3] == "###"
                and S[i + 6][j + 6 : j + 9] == "###"
                and S[i + 7][j + 6 : j + 9] == "###"
                and S[i + 8][j + 6 : j + 9] == "###"
            ):
                if (
                    S[i][j + 3] == "."
                    and S[i + 1][j + 3] == "."
                    and S[i + 2][j + 3] == "."
                    and S[i + 3][j : j + 4] == "...."
                    and S[i + 5][j + 5 : j + 9] == "...."
                    and S[i + 6][j + 5] == "."
                    and S[i + 7][j + 5] == "."
                    and S[i + 8][j + 5] == "."
                ):
                    ans.append((i + 1, j + 1))

for a in ans:
    print(*a)
