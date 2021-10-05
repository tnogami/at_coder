N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

p = 0
for i in range(N):
    p += A[i]*B[i]

if p == 0 :
    print("Yes")
else:
    print("No")

