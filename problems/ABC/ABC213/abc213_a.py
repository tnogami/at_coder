A, B = map(int, input().split())

for C in range(0,256):
    if A^C == B:
        break

print(C)