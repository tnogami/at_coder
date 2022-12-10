S = input()
T = input()
N = len(S)

for i in range(N):
    if S[i] == T[i]:
        continue
    else:
        break

print(i+1)