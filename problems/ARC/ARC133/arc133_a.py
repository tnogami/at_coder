N = int(input())
A = list(map(int,input().split()))
tmp = -1
for a in A:
    if tmp <= a:
        tmp = a 
    else:
        break

ans = []

for a in A:
    if a == tmp: continue
    ans.append(a)

print(*ans)