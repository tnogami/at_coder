N = int(input())
W = input().split()
A = ['and', 'not', 'that', 'the', 'you']
flag = False
for w in W:
    for a in A:
        if a == w:
            flag = True

if flag:
    print("Yes")
else:
    print("No")    