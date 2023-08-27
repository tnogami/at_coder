N = int(input())
P = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    m = max(P[1:])
    if P[0] > m:
        print(0)
    else:
        print(m-P[0]+1)
