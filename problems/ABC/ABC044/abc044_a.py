N = int(input())
K = int(input())
X = int(input())
Y = int(input())
ans = 0
for n in range(1,N+1):
    if n <= K:
        ans += X
    else:
        ans += Y
print(ans)