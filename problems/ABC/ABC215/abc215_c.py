import itertools
S, K = input().split()
s = [i for i in S]
ans = []
for ss in itertools.permutations(s, len(s)):
    tmp = ""
    for i in ss:
        tmp += i
    ans.append(tmp)

ans = list(set(ans))
ans.sort()
print(ans[int(K)-1])



