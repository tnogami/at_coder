S = input()

if S == S[::-1]:
    print("Yes")
else:
    Srev = S[::-1]
    a_count1 = 0
    a_count2 = 0
    flag = True
    for s in Srev:
        if s == "a":
            a_count1 += 1
        else:
            break

    for s in S:
        if s == "a":
            a_count2 += 1
        else:
            break
    if a_count1 < a_count2:
        print("No")
    else:
        diff = a_count1 - a_count2
        S = "a"*diff + S
        Srev = Srev + "a"*diff
        if S == Srev:
            print("Yes")
        else:
            print("No")


