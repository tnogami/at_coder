N = int(input())
S = input()

s = S.split("|")
if '*' in s[1]:
    print("in")
else:
    print("out")