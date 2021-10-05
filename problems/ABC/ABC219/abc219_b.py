s1 = input()
s2 = input()
s3 = input()
t = input()

ans = ""
for _t in t:
    if _t == "1":
        ans += s1
    elif _t == "2":
        ans += s2
    else:
        ans += s3

print(ans)