from collections import Counter

S = input()
T = input()

ct_s = Counter(list(S))
ct_t = Counter(list(T))


_ct_s = Counter()
_ct_t = Counter()

for i in range(97, 123):
    c = chr(i)
    if ct_s[c] == ct_t[c]:continue

    if ct_s[c] < ct_t[c]:
        _ct_t[c] = ct_t[c] - ct_s[c]
    else:
        _ct_s[c] = ct_s[c] - ct_t[c]

at_s = ct_s['@']
at_t = ct_t['@']

if set(_ct_s.keys()) <= set(list('atcoder')) and set(_ct_t.keys()) <= set(list('atcoder')):

    if sum(list(_ct_s.values())) <= at_t and sum(list(_ct_t.values())) <= at_s:
        print('Yes')
    else:
        print('No')

else:
    print("No")