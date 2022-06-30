import math
N = int(input())
X = list(map(int,input().split()))
print(sum(list(map(abs,X))))
print(math.sqrt(sum(map(lambda x:x**2, X))))
print(abs(max(X,key=lambda x:abs(x))))