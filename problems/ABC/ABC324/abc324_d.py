from collections import Counter
N = int(input())
S = input()

ct = Counter(list(S))
l = [(k, v) for k, v in ct.items()]
k_ct = len(l)
l.sort()
ans = 0
for i in range(10**7):
    s = str(i**2)
    ct_s = Counter(list(s))

    if len(s) > len(S):
        break

    if len(s) < len(S):
        ct_s['0'] += len(S) - len(s)

    is_ok = True
    k_ct_s = len(ct_s)

    if k_ct_s != k_ct:
        continue

    for k, v in ct_s.items():
        if k not in ct:
            is_ok = False
            break
        if ct[k] != v:
            is_ok = False
            break

    if is_ok:
        ans += 1

print(ans)
