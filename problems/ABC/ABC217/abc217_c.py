N = int(input())
P = list(map(int,input().split()))

ans = [0 for i in range(N)]

for i, p in enumerate(P):
    ans[p-1] = str(i+1)

print(" ".join(ans))


