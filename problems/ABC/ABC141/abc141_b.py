S = input()

for i, s in enumerate(S):
    if i%2 == 0 and s == "L":
        print("No")
        break

    if i%2 == 1 and s == "R":
        print("No")
        break
else:
    print("Yes")