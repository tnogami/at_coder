A = [tuple(map(int, input().split())) for _ in range(3)]
B = [[False]*3 for _ in range(3)]
N = int(input())

for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == A[i][j]:
                B[i][j] = True

ans = False

ans |= any([all(a) for a in B])
B = list(zip(*B))
ans |= any([all(a) for a in B])

ans |= all([B[0][0], B[1][1], B[2][2]])
ans |= all([B[0][2], B[1][1], B[2][0]])

if ans:
    print("Yes")
else:
    print("No")
