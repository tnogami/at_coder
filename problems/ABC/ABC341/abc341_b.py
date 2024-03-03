N = int(input())
A = list(map(int,input().split()))
rates = [tuple(map(int,input().split())) for _ in range(N-1)]

for i in range(N-1):
    a = A[i]
    change = (a//rates[i][0])*rates[i][1]
    A[i+1] += change

print(A[-1])