N = int(input())
st = [input().split() for i in range(N)]
s = list(map(lambda x : x[0], st))
t = list(map(lambda x : x[1], st))
S = s+t
for a in st:
    if a[0] == a[1]:
        if S.count(a[0]) == 2:
            pass
        else:
            print("No")
            break
    else:
        if S.count(a[0]) == 1 or S.count(a[1]) == 1:
            pass
        else:
            print("No")
            break
else:
    print("Yes") 
