N = int(input())
S = input()

if N == 2:
    if S == S[::-1]:
        print("Yes")
    else:
        print("No")
else:
    if S[-1] == "A":
        print("Yes")
    elif S[0] == "B":
        print("Yes")
    else:
        print("No")