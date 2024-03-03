N = int(input())
S = list(input())
Q = int(input())

# a-zまでの辞書を作成
trans = {s: s for s in 'abcdefghijklmnopqrstuvwxyz'}

for _ in range(Q):
    c, d = input().split()
    for k, v in trans.items():
        if v == c:
            trans[k] = d

ans = []

for s in S:
    ans.append(trans[s])

print(''.join(ans))