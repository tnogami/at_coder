N = int(input())
aoki = 0
takahashi = 0
for _ in range(N):
    b, a = map(int, input().split())
    aoki += a
    takahashi += b

if aoki > takahashi:
    print("Aoki")
elif aoki < takahashi:
    print("Takahashi")
else:
    print("Draw")