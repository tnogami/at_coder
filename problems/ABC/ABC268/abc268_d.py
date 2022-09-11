import itertools
N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set([input() for _ in range(M)])

num_under_bar = 16 - (sum(list(map(len, S))) + N-1)

for s in itertools.permutations(S, len(S)):
    for a in range(num_under_bar+1):
        for t in itertools.combinations_with_replacement(range(N-1), a):
            bars = ["_"] * (N-1)
            for k in t:
                bars[k] += "_"
            ans = []
            for i in range(2*N-1):
                if i%2 == 0:
                    ans.append(s[i//2])
                else:
                    ans.append(bars[i//2])
            pw = "".join(ans)
            if pw not in T and 3 <= len(pw) <= 16:
                print(pw)
                exit()
else:
    print(-1)