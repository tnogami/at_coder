N = int(input())
P = list(map(int,input().split()))

invP = P[::-1]

pre = P[-1]
for i, p in enumerate(invP):
    if pre < p:
        break
    else:
        pre = p

div = N - i
san = invP[i]
tmp = invP[:i+1]

tmp.sort()
idx = tmp.index(san)-1
ni = tmp[idx]
tmp.pop(idx)
tmp.sort(reverse=True)

print(*(P[:div-1]+[ni]+tmp))

