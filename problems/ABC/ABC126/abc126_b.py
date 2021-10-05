S = input()
a = S[0:2]
b = S[2:]

if 12 >= int(a) and int(a) != 0 and 12 >= int(b) and int(b) != 0:
    print("AMBIGUOUS")
elif 12 >= int(a) and int(a) != 0 and (12 < int(b) or int(b) == 0):
    print("MMYY")
elif 12 >= int(b) and int(b) != 0 and (12 < int(a) or int(a) == 0):
    print("YYMM")
else:
    print("NA")
