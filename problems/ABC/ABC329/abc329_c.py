N = int(input())
S = input()
S = S + ' '
d = dict()
cur = ''
ct = 0
for s in S:
    if s != cur:
        if cur not in d:
            d[cur] = ct
        else:
            d[cur] = max(d[cur], ct)
        cur = s
        ct = 1
    else:
        ct += 1

ans = 0
for k, v in d.items():
    if k == ' ' or k == '':
        continue
    ans += v


print(ans)
