N = int(input())
S = list(input())
Q = int(input())

queries = [input().split() for _ in range(Q)]
done = set()

ans = list(S)

big_or_small = 'not yet'

for query in queries[::-1]:
    if query[0] == '1':
        idx = int(query[1]) - 1
        chara = query[2]

        if idx in done:
            continue

        if big_or_small == 'not yet':
            ans[idx] = chara
            done.add(idx)
        elif big_or_small == 'big':
            ans[idx] = chara.upper()
            done.add(idx)
        else:
            ans[idx] = chara.lower()
            done.add(idx)
    else:
        if big_or_small != 'not yet':
            continue
        if query[0] == '2':
            big_or_small = 'small'

        if query[0] == '3':
            big_or_small = 'big'

if big_or_small == 'big':
    tmp = []
    for i, a in enumerate(ans):
        if i in done:
            tmp.append(a)
        else:
            tmp.append(a.upper())

    ans = tmp
elif big_or_small == 'small':
    tmp = []
    for i, a in enumerate(ans):
        if i in done:
            tmp.append(a)
        else:
            tmp.append(a.lower())
    ans = tmp

print(''.join(ans))
