from itertools import permutations

N = int(input())
S = [input() for _ in range(N)]

for comb in permutations(S, 2):
    s = comb[0] + comb[1]
    if s == s[::-1]:
        print("Yes")
        break

else:
    print("No")
