l = input().split()
l.sort()

#3,1,4,1,5,9
acc = [0,3,4,8,9,14,23]

print(acc[ord(l[1])-ord('A')]-acc[ord(l[0])-ord('A')])