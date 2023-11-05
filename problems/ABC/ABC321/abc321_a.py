N = input()
init = 10
for n in N:
    if int(n) >= init:
        print("No")
        break
    init = int(n)
else:
    print("Yes")
