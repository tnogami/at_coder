N, Q = map(int, input().split())
follows = dict()

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if A in follows:
            follows[A].add(B)
        else:
            follows[A] = set([B])
    elif T == 2:
        if A in follows:
            if B in follows[A]:
                follows[A].remove(B)
    else:
        if A in follows:
            if B in follows[A]:
                if B in follows:
                    if A in follows[B]:
                        print("Yes")
                        continue
        print("No")

