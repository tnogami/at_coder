S = list(input())
N = int(input())

bottom = 0

digit = 0
for s in S[::-1]:
    if s == '?':
        digit += 1 
        continue
    if s == '1':
        bottom += 2**digit

    digit += 1

M = len(S)
M -= 1

if bottom > N:
    print(-1)
else:
    for s in S:
        if s != '?':
            M -= 1
            continue
        if bottom + 2**M <= N:
            bottom += 2**M
        M -= 1

    print(bottom)

