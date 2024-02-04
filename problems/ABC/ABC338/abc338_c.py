N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

for a in range(10**6+5):
    a_is_ok = True
    b_min = 10**10
    for n in range(N):
        if A[n] * a > Q[n]:
            a_is_ok = False
            break

        if B[n] == 0:
            continue
        b_min = min(b_min, (Q[n] - A[n] * a)//B[n])

    if a_is_ok:
        ans = max(ans, a + b_min)

print(ans)
