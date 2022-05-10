N = int(input())
ans = 0
for i in range(100):
    for j in range(100):
        if 4*i+7*j==N:
            ans+=1
if ans:
    print("Yes")
else:
    print("No")