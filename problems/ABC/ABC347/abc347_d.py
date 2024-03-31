a, b, C = map(int, input().split())

C_bin = bin(C)[2:]
C_bin = '0' * (60-len(C_bin)) + C_bin

ct_zero = 0

for c in C_bin:
    if c == '0':
        ct_zero += 1


