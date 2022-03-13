V, A, B, C = map(int, input().split())
use = [A,B,C]
for i in range(1000000):
    V -= use[i%3]
    if V < 0: break
if i%3==0:
    print("F")
elif i%3==1:
    print("M")
else:
    print("T")