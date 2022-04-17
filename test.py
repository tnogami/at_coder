import time
import sys
sys.setrecursionlimit(10**9)
MOD = 998244353

def Fib(n):
    global memo
    if n in memo:
        return memo[n]
    else:
        memo[n] = (Fib(n-1) + Fib(n-2))%MOD
        return memo[n]

N = int(input())
start = time.time()
# 計測したい処理
memo = {0:1, 1:1, 2:3}
Fib(100000)
e_time = time.time() - start

print("hello")
print ("e_time:{0}".format(e_time*1000) + "[ms]")
