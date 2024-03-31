
N = int(input())
ans = 1
for n in range(2, min(N+1, 10**6+5)):
    k = n**3
    if k > N:
        break

    if len(str(k)) == 1:
        ans = k
        continue

    if str(k) == str(k)[::-1]:
        ans = k
        continue

print(ans)
