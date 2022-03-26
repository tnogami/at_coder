N = int(input())
T = input()

dir = "E"
x = 0
y = 0

for t in T:
    if t == "S":
        if dir == "E":
            x += 1
        elif dir == "W":
            x -= 1
        elif dir == "N":
            y += 1
        elif dir == "S":
            y -= 1
    else:
        if dir == "E":
            dir = "S"
        elif dir == "W":
            dir = "N"
        elif dir == "N":
            dir = "E"
        elif dir == "S":
            dir = "W"

print(x, y)

        

