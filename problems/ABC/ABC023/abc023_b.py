N = int(input())
S = input()

for i in range(1000):

    if i == 0:
        acs = "b"
    elif i%3 == 1:
        acs = "a" + acs + "c"
    elif i%3 == 2:
        acs = "c" + acs + "a"
    else:
        acs = "b" + acs + "b"

    if acs == S: 
        print(i)
        break
else:
    print(-1)



