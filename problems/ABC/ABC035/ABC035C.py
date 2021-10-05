import itertools
N, Q = map(int, input().split())
othellos = [0 for i in range(N)]
for i in range(Q):
    l, r = map(int, input().split())
    othellos[l-1] += 1
    if r == N :continue
    othellos[r] -= 1
othellos = [str(i%2) for i in itertools.accumulate(othellos)]
print("".join(othellos))