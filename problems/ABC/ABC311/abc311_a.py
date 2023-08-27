N = int(input())
S = input()

G = set()

for i, s in enumerate(S, 1):
    G.add(s)
    if len(G) == 3:
        print(i)
        break
