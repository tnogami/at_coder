S = input()
for i,c in enumerate(S):
    if i%2 == 0 and c.isupper():
        print("No")
        break

    if i%2 == 1 and c.islower():
        print("No")
        break
else:
    print("Yes")