N = int(input())
S = input()

cur = S[0]
if len(S) == 1:
    print("Yes")
else:
    for s in S[1:]:
        if s == cur:
            print("No")
            break

        cur = s
    else:
        print("Yes")
