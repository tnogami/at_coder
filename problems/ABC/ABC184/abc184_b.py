N, X = map(int, input().split())
S = input()

for s in S:
    if s == "x" and 0 < X: X -= 1
    if s == "o" : X += 1

print(X)