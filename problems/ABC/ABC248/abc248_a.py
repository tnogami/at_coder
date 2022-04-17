S = input()
num = [i for i in range(10)]
for s in S:
    num.remove(int(s))

print(num[0])