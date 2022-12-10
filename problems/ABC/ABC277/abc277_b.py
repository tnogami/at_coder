N = int(input())
S = [input() for _ in range(N)]

flag = True

first = ["H" , "D" , "C" , "S"]
second = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"] 

for s in S:
    if s[0] not in first:
        flag = False
    if s[1] not in second:
        flag = False

if len(S) != len(set(S)):
    flag = False

if flag:
    print("Yes")
else:
    print("No")
