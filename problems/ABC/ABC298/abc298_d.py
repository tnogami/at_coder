from collections import deque

MOD = 998244353
Q = int(input())
dq = deque('1')

num = 1
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        dq.append(query[1])
        num *= 10
        num += int(query[1])
        num %= MOD
    elif query[0] == 2:
        digit = len(dq)
        s = int(dq.popleft())
        num -= s*pow(10, (digit-1), MOD)
        num %= MOD
    else:
        num %= MOD
        print(num)
        