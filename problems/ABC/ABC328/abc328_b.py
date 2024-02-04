N = int(input())
D = list(map(int, input().split()))

ans = 0
for n in range(1, N+1):
    for d in range(1, D[n-1]+1):
        # ゾロ目の場合
        if len(set(list(str(d)))) == 1 and len(set(list(str(n)))) == 1 and list(str(n))[0] == list(str(d))[0]:
            ans += 1
print(ans)