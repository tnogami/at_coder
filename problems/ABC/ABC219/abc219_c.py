import string
from collections import defaultdict
newdic = defaultdict(str)

ALPHA = string.ascii_lowercase

X = input()
N = int(input())

namelist = []

for i,x in enumerate(X):
    newdic[x] = ALPHA[i]

for i in range(N):
    oldname = input()
    tmpname = ""
    for j in oldname:
        tmpname += newdic[j]
    namelist.append((oldname, tmpname))

namelist.sort(key = lambda x:x[1])

for ans in namelist:
    print(ans[0])


