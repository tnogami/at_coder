S = input()

a = 0
b = 0
n = 1
for i in range(len(S)):
    if S[i] != str(n%2):
        a += 1
    else:
        b += 1
    n += 1
print(min(a,b))
