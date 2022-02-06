T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    if s-2*a >= 0 and (s-2*a)&a == 0:
        print("Yes")
    else:
        print("No")
    # a = bin(a)[2:].zfill(63)[::-1]
    # s = bin(s)[2:].zfill(63)[::-1]
    # up = False
    # flag = False
    # for i in range(62):
    #     if s[i] == "0":
    #         if up == False and a[i] == "1":
    #             up = True
    #         elif up == True and a[i] == "0":
    #             up = True
    #         elif up == False and a[i] == "0":
    #             up = False
    #         elif up == True and a[i] == "1":
    #             flag = True
    #             break
    #     else:
    #         if up == False and a[i] == "1":
    #             flag = True
    #             break
    #         elif up == True and a[i] == "0":
    #             up = False
    #         elif up == False and a[i] == "0":
    #             up = False
    #         elif up == True and a[i] == "1":
    #             up = True
    # if up or flag:
    #     print("No")
    # else:
    #     print("Yes")


