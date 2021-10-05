N = int(input())

V = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
for i in range(N):
    tmp = V[i]-C[i]
    if 0 < tmp : ans += tmp

print(ans)
