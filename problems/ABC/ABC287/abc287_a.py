N = int(input()) 
ct = 0
for _ in range(N):
    s = input()
    if s == "For":
        ct += 1

if N//2 < ct:
    print("Yes")
else:
    print("No")