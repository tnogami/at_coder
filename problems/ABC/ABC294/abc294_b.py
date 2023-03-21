H, W = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(H)]

ans = []

for a in A:
    tmp = ''
    for b in a:
        if b == 0:
            tmp += '.'
        else:
            tmp += chr(ord('A')+b-1)

    ans.append(tmp)

for a in ans:
    print(a)