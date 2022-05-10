a,b = map(int, input().split())

diff = b - a

hight = diff*(diff+1)//2

print(hight-b)