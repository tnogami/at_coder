N = int(input())
name = set()
for i in range(N):
    i += 1
    s = input()
    if not s in name:
        print(i)
        name.add(s)
