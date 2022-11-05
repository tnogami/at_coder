from itertools import combinations

def check(comb):
    d = dict()
    for c in combinations(comb, 2):
        dist = (c[0][0]-c[1][0])**2 + (c[0][1]-c[1][1])**2
        if dist in d:
            d[dist] += 1
        else:
            d[dist] = 1

    if len(d) == 2:
        L = list(d.values())
        if (L[0] == 2 and L[1] == 4) or (L[0] == 4 and L[1] == 2):
            return True
    return False
    

S = [input() for _ in range(9)]

pons = []

for j,s in enumerate(S):
    for i,c in enumerate(s):
        if c == "#":
            pons.append((j,i))


ans = 0
for comb in combinations(pons, 4):
    if check(comb) : ans += 1

print(ans)