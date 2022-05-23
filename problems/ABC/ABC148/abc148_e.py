N = int(input())
if N%2 == 1:
    print(0)
else:
    N //= 5
    N //= 2
    ans = N
    while N != 0:
        N //= 5
        ans += N
    print(ans)