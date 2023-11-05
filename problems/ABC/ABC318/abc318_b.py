from dataclasses import field


N = int(input())
field = [[0]*100 for _ in range(100)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    for i in range(A, B):
        for j in range(C, D):
            field[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        ans += field[i][j]

print(ans)
