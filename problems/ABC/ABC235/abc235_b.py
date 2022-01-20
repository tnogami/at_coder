N = int(input())
H = list(map(int,input().split()))
cur = 0

for h in H :
    if cur < h:
        cur = h
    else:
        break

print(cur)