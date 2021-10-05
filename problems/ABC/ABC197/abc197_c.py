N = int(input())
A = list(map(int,input().split()))

# ０１の数(2^20 ≒ 10^6なので最大でもN=20程度)
# 3桁の場合 0b111= 7 なので range(8)=range(2**3)のループ
N -= 1
out = 2**35
for i in range(2**N): #01の組み合わせ
    ans = 0
    tmp = A[0]
    for j in range(N):  # シフト回数ループ
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            ans = ans^tmp
            tmp = A[j+1]
        else:
            tmp = tmp|A[j+1]
    ans = ans^tmp
    out = min(out ,ans)

print(out)


