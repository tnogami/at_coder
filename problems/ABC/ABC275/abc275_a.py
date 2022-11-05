N = int(input())
H = list(map(int,input().split()))
highest = max(H)

for i, h in enumerate(H):
    if h == highest:
        print(i+1)
        break