N = input()

if len(N) < 4:
    print(N)
else:
    L = len(N)
    L -= 3
    ans = N[:-L] + '0'*L
    print(ans)