N = int(input())
A = list(map(int,input().split()))
divd = [0]
ang = 0
for a in A:
    ang += a
    ang %= 360
    divd.append(ang)

divd.sort()
ans = 0
for i in range(N):
    ans = max(ans, divd[i+1]-divd[i])
print(max(ans, 360-divd[-1]))
