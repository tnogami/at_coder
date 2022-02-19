N = int(input())
ans = []
while N !=0 :
    N -= 1
    ans.append(chr(ord("a") + N%26))
    N //= 26

print("".join(ans[::-1]))
