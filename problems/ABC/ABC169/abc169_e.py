N = int(input())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()
ans = 0
if N % 2 == 0:
    AX = A[N // 2] + A[N // 2 - 1]
    BX = B[N // 2] + B[N // 2 - 1]
    ans = BX - AX + 1
else:
    AX = A[N // 2]
    BX = B[N // 2]
    ans = BX - AX + 1
print(ans)

