S = [input() for _ in range(10)]

for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            a = i+1
            c = j+1

for i in range(9, -1, -1):
    for j in range(9, -1, -1):
        if S[i][j] == "#":
            b = i+1
            d = j+1

print(a,b)
print(c,d)