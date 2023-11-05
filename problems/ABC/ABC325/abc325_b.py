N = int(input())
WX = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(24):
    can_attend = 0
    for n in range(N):
        cur_time = WX[n][1] + i
        cur_time %= 24
        if 9 <= cur_time <= 17:
            can_attend += WX[n][0]
    ans = max(ans, can_attend)

print(ans)
