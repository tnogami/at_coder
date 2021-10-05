N = input()
s = 0
for n in N:
    s += int(n)
if s % 9 == 0:
    print("Yes")
else:
    print("No")
