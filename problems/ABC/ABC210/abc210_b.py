N = int(input())
S = input()

for i, s in enumerate(S):
    if s == "1":
        if i%2 == 1:
            print("Aoki")
        else:
            print("Takahashi")

        break