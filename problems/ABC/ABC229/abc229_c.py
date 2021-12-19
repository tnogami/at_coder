N, W = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N)]

AB.sort(reverse=True)

ans = 0
for a, b in AB:
    if W <= b:
        ans += a*W
        break
    else:
        ans += a*b
        W -= b

print(ans)

