MOD = 1000000007

N, Q = map(int, input().split())

A = [[] for _ in range(60)]
for _ in range(Q):
    x, y, z, w = map(int, input().split())
    for shift in range(60):
        bit = (w >> shift) & 1
        A[shift].append((x-1,y-1,z-1,bit))

ans = 1
for shift in range(60):
    tmp = 0
    for n in range(2**N):
        is_ok = True
        for a in A[shift]:
            x, y, z, bit = a
            if (n>>x)&1 | (n>>y)&1 | (n>>z)&1 != bit : is_ok = False
        if is_ok : tmp += 1

    ans *= tmp
    ans %= MOD

print(ans)



        






