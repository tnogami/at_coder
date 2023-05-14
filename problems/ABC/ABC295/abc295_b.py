from copy import deepcopy

R, C = map(int, input().split())

field = [list(input()) for _ in range(R)]

ans = deepcopy(field)

for r in range(R):
    for c in range(C):
        if field[r][c].isdecimal():
            n = int(field[r][c])
            ans[r][c] = '.'
            for i in range(-n, n+1):
                for j in range(-n, n+1):
                    if n < abs(i)+abs(j): continue
                    new_i = r + i
                    new_j = c + j
                    if new_i < 0 or R <= new_i or new_j < 0 or C <= new_j: continue
                    ans[new_i][new_j] = '.'


for a in ans:
    print("".join(a))