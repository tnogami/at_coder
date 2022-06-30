H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

dp = [[10**6]*(W+2) for _ in range(H+2)]
dp[H][W] = 0

for w in range(W, 0, -1):
    for h in range(H, 0, -1):
        pm = 1
        if field[h-1][w-1] == "-":
            pm *= -1
            
        if (h+w)%2 == 0: #Aoki turn
            #左に配る
            dp[h][w-1] = dp[h][w] - pm

            #上に配る
            if dp[h-1][w] == 10**6:
                dp[h-1][w] = dp[h][w] - pm
            else:
                if dp[h-1][w] > dp[h][w] - pm:
                    dp[h-1][w] = dp[h][w] - pm                    

        else: #Takahashi turn
            #左に配る
            dp[h][w-1] = dp[h][w] + pm

            #上に配る
            if dp[h-1][w] == 10**6:
                dp[h-1][w] = dp[h][w] + pm
            else:
                if dp[h-1][w] < dp[h][w] + pm:
                    dp[h-1][w] = dp[h][w] + pm


if dp[1][1] == 0:
    print("Draw")
elif 0 < dp[1][1]:
    print("Takahashi")
else:
    print("Aoki")        





