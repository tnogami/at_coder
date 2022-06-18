N = int(input())
ans = 0
for i in range(1,N+1):
    for k in range(2,N+1):
        if i < k**2 : break
        while i%(k**2) == 0:
            i //= k**2
    for j in range(1, N+1):
        if i*j**2 <= N:
            ans += 1
        else:
            break

print(ans)