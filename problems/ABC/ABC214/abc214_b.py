S, T = map(int, input().split())
ans = 0
for a in range(0, S+1):
    for b in range(0, S+1):
        for c in range(0, S+1):
            m = a+b+c
            p = a*b*c
            if m <= S and p <=T: ans+=1
    
print(ans)