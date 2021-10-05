s = input()
N = int(input())
for i in range(N):
    l, r = map(int, input().split())
    left = s[:l-1]
    center = s[l-1:r]
    right = s[r:]
    s = left + center[::-1] + right

print(s)