N = int(input())
yakusu = [i for i in range(1, 10) if N % i == 0]

ans = []
for i in range(N+1):
    for m in yakusu:
        if i % (N//m) == 0:
            ans.append(str(m))
            break
    else:
        ans.append('-')

print(''.join(ans))
