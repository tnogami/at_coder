K = int(input())
A, B = input().split()

A = A[::-1]
B = B[::-1]

aa = 0
bb = 0
for i, a in enumerate(A):
    aa += int(a)*(K**i)

for i, b in enumerate(B):
    bb += int(b)*(K**i)

print(aa*bb)

