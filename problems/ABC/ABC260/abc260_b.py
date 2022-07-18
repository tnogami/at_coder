N, X, Y, Z = map(int, input().split())
math = list(map(int,input().split()))
english = list(map(int,input().split()))

passed = [False]*N
ans = []
scores =[]

for i in range(N):
    scores.append((i, math[i], english[i]))

scores.sort(key=lambda x:x[1], reverse=True)

idx = 0
while X != 0:
    if passed[scores[idx][0]] :
        idx += 1
        continue
    ans.append(scores[idx][0])
    passed[scores[idx][0]] = True
    X -= 1
    idx += 1

scores.sort()
scores.sort(key=lambda x:x[2], reverse=True)
idx = 0
while Y != 0:
    if passed[scores[idx][0]] : 
        idx += 1
        continue
    ans.append(scores[idx][0])
    passed[scores[idx][0]] = True
    Y -= 1
    idx += 1

scores.sort()
scores.sort(key=lambda x:x[1]+x[2], reverse=True)
idx = 0
while Z != 0:
    if passed[scores[idx][0]] :
        idx += 1
        continue
    ans.append(scores[idx][0])
    passed[scores[idx][0]] = True
    Z -= 1
    idx += 1

    
ans.sort()

for a in ans:
    print(a+1)