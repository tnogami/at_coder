L, R = map(int, input().split())
S = input()
print(S[0:L-1]+S[L-1:R][::-1]+S[R:])


