N, Q = map(int, input().split())
pena = [0]*N

for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        pena[x-1] += 1
    elif q == 2:
        pena[x-1] += 2
    else:
        if 2 <= pena[x-1]:
            print("Yes")
        else:
            print("No")