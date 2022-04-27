A, B, C = map(int, input().split())
K = int(input())

s = A+B+C
m = max(A,B,C)
s -= m
print(s+m*2**K)

