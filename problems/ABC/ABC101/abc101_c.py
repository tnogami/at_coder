N, K = map(int, input().split())
a = list(map(int, input().split()))
idx = 1
rest = N - K
while 0 < rest:
    rest -= (K-1)
    idx += 1

print(idx)