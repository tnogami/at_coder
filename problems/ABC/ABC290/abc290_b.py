
N, K = map(int, input().split())
S = input()

ans = []
ct = 0
for i, s in enumerate(S):
    if s == 'x' or ct == K:
        ans.append('x')
    else:
        ans.append('o')
        ct += 1

print("".join(ans))
