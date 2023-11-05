N, M = map(int, input().split())
S = input()
T = input()

prefix = T[:N]
suffix = T[-N:]

if prefix == S and suffix == S:
    print(0)
elif prefix == S:
    print(1)
elif suffix == S:
    print(2)
else:
    print(3)
