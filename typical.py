import string
ct = 0
al = [""] + [i for i in string.ascii_lowercase]
for i in al:
    for j in al[1:]:
        print(i, j)
        f = open("./problems/typical90/typical90_" + i + j + ".py", "w")
        ct += 1
        if ct == 90:break
    if ct == 90:break