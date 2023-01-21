N, X = map(int, input().split())
coin2num = dict()
prices = []
for _ in range(N):
    A, B = map(int, input().split())
    prices.append(A)
    coin2num[A] = B

dp = [[False]*(10**4+5) for _ in range(N+1)]
for n in range(N+1):
    dp[n][0] = True

for i in range(N):
    price = prices[i]
    num = coin2num[price]
    for k in range(10**4+5):
        if dp[i][k] == False:continue

        for m in range(num+1):
            if 10**4+3 < k+price*m:break
            dp[i+1][k+price*m] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")
        
