N = int(input())
H = list(map(int,input().split()))

a = H[0]

if a != 0: a-=1

for b in H[1:]:
    if a == b:continue
    if a+1 == b: continue
    
    if a+1 < b:
        a = b-1
        continue

    if a+1 > b:
        print("No")
        break
else:
    print("Yes")
