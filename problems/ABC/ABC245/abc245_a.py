A, B, C, D = map(int, input().split())
t = 60*A + B
a = 60*C + D + 0.1

if t < a:
    print("Takahashi")
else:
    print("Aoki")