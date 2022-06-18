MOD = 998244353

N, M = map(int, input().split())

#Mはm桁の2進数. m = 2 のとき M < 4(100) なので2桁 11 or 10 or 01.
for m in range(70):
    if M < 2**m:
        m_digit = m
        break

#2進数でM以下かつi桁の数を計算しておく
keta = dict()
for i in range(m_digit-1):
    keta[i+1] = 2**i
#m桁の数はMの最上位bitを0にした数にゼロを考慮して1プラスする。
keta[m_digit] = (M^(1 << (m_digit-1))) + 1

#dp[i][j] A_iがj桁の値となる場合の数
dp = [[0]*(m_digit+1) for _ in range(61)]

#A_1は1~m桁の初期値を代入
for i in range(1, m_digit+1):
    dp[1][i] = keta[i]

for n in range(1,60):
    for i in range(1, m_digit+1):
        for k in range(i+1, m_digit+1):
            dp[n+1][k] += dp[n][i]*keta[k]
            dp[n+1][k] %= MOD

if 70 < N:
    print(0)
else:
    print(sum(dp[N][:m_digit+1])%MOD)

