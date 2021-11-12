n = list(map(int, input().split(".")))
s = str(n[1])
if 5 <= int(s[0]):
    print(n[0]+1)
else:
    print(n[0])