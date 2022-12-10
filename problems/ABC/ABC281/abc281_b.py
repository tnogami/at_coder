S = input()
if len(S) != 8:
    print("No")
else:
    a = S[0]
    b = S[1:7]
    c = S[7]
    if a.isalpha() and c.isalpha() and b.isdecimal():
        if 100000 <= int(b) and int(b) <= 999999:
            print("Yes")
        else:
            print("No")
    else:
        print("No")