S = input()
ans = 0
for s in S:
    if s == "+": ans+=1
    if s == "-": ans-=1

print(ans)