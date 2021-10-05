N = int(input())
A = list(map(int,input().split()))
X = int(input())
sumA = sum(A)
ans = N*(X//sumA)
X -= sumA*(X//sumA)
tmp = 0
for a in enumerate(A):
    ans += 1
    tmp += a
    if X < tmp:
        print(ans)
        break
