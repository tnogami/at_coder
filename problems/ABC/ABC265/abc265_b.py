N, M, T = map(int, input().split())
A = list(map(int,input().split()))
bonus = {m[0]-1:m[1] for m in [tuple(map(int, input().split())) for _ in range(M)]}

for i, a in enumerate(A):
    if i in bonus: T += bonus[i]
    T -= a
    if T <= 0:
        print("No")
        break
else:
    print("Yes")