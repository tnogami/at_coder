S = input()
for s in S:
    if S.count(s) == 1:
        print(s)
        break
else:
    print(-1)