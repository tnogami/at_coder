N = int(input())
if N <= 999:
    num = str(N).zfill(3)
    print("ABC")
else:
    num = str(N-999).zfill(3)
    print("ABD")