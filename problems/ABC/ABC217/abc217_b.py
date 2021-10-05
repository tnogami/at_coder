
l = ["ABC", "ARC", "AGC", "AHC"]
ll =[] 

for i in range(3):
    tmp = input()
    ll.append(tmp)

for i in l:
    if not i in ll:
        print(i)

