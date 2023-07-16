N, K = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(N)]

n = sum(map(lambda x: x[1], AB))
AB.sort()

if n <= K:
    print(1)
else:
    for ab in AB:
        n -= ab[1]
        if n <= K:
            print(ab[0]+1)
            break
