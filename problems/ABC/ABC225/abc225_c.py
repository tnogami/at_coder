N, M = map(int, input().split())

B = [list(map(int, input().split())) for i in range(N)]

ans = True

for i in range(N):
    for j in range(M-1):
        j1 = (B[i][j]-1)%7+1
        i1 = (B[i][j] - j1)//7
        j2 = (B[i][j+1]-1)%7+1
        i2 = (B[i][j+1] - j2)//7
        if B[i][j+1] != B[i][j]+1 or i1 != i2:
            ans = False

for j in range(M):
    for i in range(N-1):
        if B[i+1][j] != B[i][j] + 7:
            ans = False

if ans:
    print("Yes")
else:
    print("No")
