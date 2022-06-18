N = int(input())
S = input().split()

for s in S:
    if s == "Y":
        print("Four")
        break
else:
    print("Three")