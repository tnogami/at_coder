S = input()

pattern = []
for i in range(len(S)):
    for j in range(i, len(S)):
        s = S[i:j+1]
        if s not in pattern:
            pattern.append(s)

print(len(pattern))