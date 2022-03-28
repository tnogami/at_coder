N, M = map(int, input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = [C[-1]//A[-1]]

for i in range(M):
    c = C[-i-2]
    for j in range(i+1):
        if N <= -i-2+j or -i-2+j < -(N+1) : continue
        c -= ans[j]*A[-i-2+j]
    ans.append(c//A[-1])

print(*ans[::-1])
