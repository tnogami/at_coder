N = int(input())
used = [False] * (2*N+2)

for n in range(1, 2*N+2):
    if used[n] == True:
        continue
    else:
        print(n, flush=True)
        used[n] = True
        k = int(input())
        used[k] = True
