R, C = map(int, input().split())
A = [tuple(map(int,input().split())) for _ in range(2)]
print(A[R-1][C-1])