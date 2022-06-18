N = input()
f = sum(map(int, list(N)))
if int(N)%f == 0:
    print("Yes")
else:
    print("No")